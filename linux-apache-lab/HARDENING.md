# SSH and host hardening guide

> **Status:** step-by-step guide that I have not run yet. The Results sections are empty on purpose and would be filled in with real output if I run it.

Host: fresh DigitalOcean droplet, Ubuntu 22.04. Starting point: SSH as root with a password, Apache installed with its packaged defaults, serving a custom `index.html` on port 80.

Replace `SERVER_IP` with the droplet's public IPv4 address before any command run from your computer. The sudo account in this lab is `deploy`. If you choose another name, use it in every later command.

## Warning

Keep the original root SSH session open until the new-login test in step 3 has succeeded. Do the deploy-user test in a second terminal, and leave that session open too.

Do the steps in order. Leave root SSH and password SSH in place until a key login as `deploy` has worked. Leave UFW off until the OpenSSH allow rule is in place.

If SSH stops accepting connections, open the DigitalOcean Droplet Console: control panel, this droplet, Access, Launch Droplet Console. That console is a virtual screen, separate from `sshd`. The account password still works there after `PasswordAuthentication no`. Resetting the root password from the DigitalOcean panel reboots the droplet. Use that only if the console password fails.

Record output in each Results section from the commands you ran. Leave a section empty until you run that step. Do not put passwords or private keys in the write-up.

## 1. Create a non-root sudo user

**Why.** Later steps close root SSH, so the account you will use has to exist and be able to `sudo` first.

**Commands.** On the droplet, in the original root session. `adduser` asks for a password, then full name, room number, and phone numbers. The password is what `sudo` will ask for. Press Enter through the name and phone fields.

```bash
sudo adduser deploy
sudo usermod -aG sudo deploy
```

**Verify.**

```bash
id deploy
getent group sudo
```

`id` should list the group `sudo`. The `sudo` line from `getent` should contain `deploy`.

**If it goes wrong.** If `adduser` says the user exists, pick another name and use it for the rest of the lab. Do not delete root. Do not edit `/etc/sudoers` by hand. If `deploy` is missing from group `sudo`, rerun `sudo usermod -aG sudo deploy` and check `getent group sudo` again. A session opened before that `usermod` does not gain the group until you log in again.

### Results

<!-- Write what you actually saw. -->

## 2. SSH key authentication

**Why.** Step 3 turns off password login, so the key has to work before that change.

**Commands.** On your computer. `ssh-keygen` asks for a passphrase. Set one. If it says the file already exists, answer `n` and pick a different `-f` path, then use that path below.

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_droplet -C "deploy@droplet"
command -v ssh-copy-id
```

If `command -v` printed a path:

```bash
ssh-copy-id -i ~/.ssh/id_ed25519_droplet.pub deploy@SERVER_IP
```

If `command -v` printed nothing:

```bash
ssh deploy@SERVER_IP 'mkdir -p ~/.ssh && chmod 700 ~/.ssh'
cat ~/.ssh/id_ed25519_droplet.pub | ssh deploy@SERVER_IP 'cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys'
```

Both forms ask for the `deploy` password from step 1. Password login is still on, and this step needs it. Copy only the `.pub` file. Leave the private key on your computer.

**Verify.** Open a second terminal on your computer. Leave the root session alone.

```bash
ssh -i ~/.ssh/id_ed25519_droplet -o IdentitiesOnly=yes deploy@SERVER_IP
```

In that session:

```bash
whoami
sudo whoami
```

`whoami` should print `deploy`. `sudo whoami` asks for the `deploy` password and should print `root`.

Do not start step 3 until both have succeeded. Leave both terminals open.

**If it goes wrong.** Use the root session to inspect the key file:

```bash
ls -ld /home/deploy /home/deploy/.ssh
ls -l /home/deploy/.ssh/authorized_keys
```

`.ssh` should be mode `700`, owner `deploy:deploy`. `authorized_keys` should be mode `600`, owner `deploy:deploy`, with one line starting with `ssh-ed25519`. Repair with:

```bash
sudo chown -R deploy:deploy /home/deploy/.ssh
sudo chmod 700 /home/deploy/.ssh
sudo chmod 600 /home/deploy/.ssh/authorized_keys
```

Retry the second terminal. If `sudo whoami` says `deploy` is not allowed to use sudo, run `sudo usermod -aG sudo deploy` from the root session and open a new `deploy` SSH session. For the server's reason:

```bash
sudo journalctl -u ssh -n 30 --no-pager
```

Look for ownership or permission lines. That log contains usernames and source addresses, so keep it out of a public write-up.

### Results

<!-- Write what you actually saw. -->

## 3. Disable root login and password authentication

**Why.** Password guessing and root SSH should have no path in once a key login works.

**Commands.** Run this from the original root session. Ubuntu 22.04 includes `/etc/ssh/sshd_config.d/*.conf` near the top of `sshd_config`, and `sshd` keeps the first value it sees for each keyword. Cloud images often ship `50-cloud-init.conf` containing `PasswordAuthentication yes`. A `no` written only in `/etc/ssh/sshd_config` loses to that file. `00-hardening.conf` sorts first, so its values win.

`sshd -t` checks syntax and prints nothing when the file is valid. `sshd -T` prints the values that won.

Record the current state:

```bash
sudo ls -l /etc/ssh/sshd_config.d/
sudo sshd -T | grep -E '^(permitrootlogin|passwordauthentication|kbdinteractiveauthentication|challengeresponseauthentication|pubkeyauthentication) '
sudo grep -n -E 'Match|PasswordAuthentication|PermitRootLogin|KbdInteractiveAuthentication|ChallengeResponseAuthentication|PubkeyAuthentication' /etc/ssh/sshd_config /etc/ssh/sshd_config.d/*.conf
```

If `ls` shows an empty directory, run the `grep` on `/etc/ssh/sshd_config` only. A line with a leading `#` is a comment. If `grep` shows a `Match` block, read it before continuing. A `Match` can allow passwords for some logins while the global value is `no`.

```bash
sudo tee /etc/ssh/sshd_config.d/00-hardening.conf >/dev/null <<'EOF'
# Sorted first so these win over 50-cloud-init.conf. sshd keeps the first value.
PermitRootLogin no
PasswordAuthentication no
KbdInteractiveAuthentication no
PubkeyAuthentication yes
EOF
sudo sshd -t
sudo sshd -T | grep -E '^(permitrootlogin|passwordauthentication|kbdinteractiveauthentication|challengeresponseauthentication|pubkeyauthentication) '
```

Reload only if `sudo sshd -t` exits 0 and prints nothing, and `sshd -T` shows:

```
permitrootlogin no
passwordauthentication no
pubkeyauthentication yes
```

plus keyboard-interactive off. That line is `kbdinteractiveauthentication no`. If that name is absent, `challengeresponseauthentication no` is the same setting. Reload only when the printed one is `no`.

```bash
sudo systemctl reload ssh
```

On Ubuntu 22.04 the unit name is `ssh`. From a third terminal on your computer, confirm the key still works:

```bash
ssh -i ~/.ssh/id_ed25519_droplet -o IdentitiesOnly=yes -o PreferredAuthentications=publickey deploy@SERVER_IP
```

Then confirm password login fails. If either command logs you in, stop and use the recovery commands below.

```bash
ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no -o NumberOfPasswordPrompts=1 deploy@SERVER_IP
ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no -o NumberOfPasswordPrompts=1 root@SERVER_IP
```

The `deploy` password still works for `sudo` on the server.

Optional. This tells cloud-init not to write `PasswordAuthentication yes` back into its drop-in on a later run. Skip it if the directory is missing. `00-hardening.conf` is what changes SSH now.

```bash
if [ -d /etc/cloud/cloud.cfg.d ]; then
  printf '%s\n' 'ssh_pwauth: false' | sudo tee /etc/cloud/cloud.cfg.d/99-ssh-pwauth.cfg >/dev/null
fi
```

Leave `UsePAM` at its current value.

**Verify.**

```bash
sudo sshd -T | grep -E '^(permitrootlogin|passwordauthentication|kbdinteractiveauthentication|challengeresponseauthentication|pubkeyauthentication) '
systemctl is-active ssh
```

`is-active` should print `active`. The key login from the third terminal should succeed. Both password commands should fail and should not open a shell.

**If it goes wrong.** Do this from the original root session. If `sshd -t` prints an error, or `sshd -T` does not show the required values, do not reload. If you already reloaded and the new key login fails:

```bash
sudo rm /etc/ssh/sshd_config.d/00-hardening.conf
sudo sshd -t && sudo systemctl reload ssh
```

If `sshd -t` says `Missing privilege separation directory: /run/sshd`:

```bash
sudo mkdir -p -m 0755 /run/sshd
sudo sshd -t
```

If `systemctl reload ssh` says the unit was not found:

```bash
systemctl list-unit-files 'ssh*'
```

Reload the unit name that list shows. On Ubuntu 22.04 it is `ssh`. If the root SSH session is already dead, remove `00-hardening.conf` from the Droplet Console and reload `ssh`.

If `sshd -T` still shows `passwordauthentication yes`, another file was read first. The `grep` of `sshd_config.d` shows which one. Change that line, or rename the hardening file so it sorts earlier, then run `sshd -t` and `sshd -T` again before any reload.

### Results

<!-- Write what you actually saw. -->

## 4. Enable UFW

**Why.** Anything not in an allow rule should be dropped, and SSH has to be one of those rules before the filter is switched on.

**Commands.** On the droplet. The default policies do not enable the firewall. The allow order is OpenSSH, then HTTP, then HTTPS. Enable is last.

```bash
command -v ufw || sudo apt-get install -y ufw
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow OpenSSH
sudo ufw allow 80/tcp comment 'HTTP'
sudo ufw allow 443/tcp comment 'HTTPS'
sudo ufw status verbose
sudo ufw show added
```

While UFW is inactive, `status verbose` prints only `Status: inactive` and does not list any rules. `ufw show added` lists the rules you have queued. Confirm it shows OpenSSH (or 22/tcp), 80/tcp, and 443/tcp before enabling. Then:

```bash
sudo ufw enable
sudo ufw status verbose
```

`ufw enable` asks for confirmation. Answer `y`. From the second terminal, run a command to confirm that session is still up, and open one new key login from your computer before closing either session.

The OpenSSH profile is 22/tcp. This lab does not change the SSH port. If you change `Port` later, allow that port in UFW before reloading `sshd`.

**Verify.**

```bash
sudo ufw status verbose
```

Status should be active, the incoming default should be deny, and 22/tcp, 80/tcp, and 443/tcp should be allowed. Ubuntu's default `/etc/default/ufw` has `IPV6=yes`, so the same rules appear for v6. Record whether yours do.

From your computer:

```bash
curl -sI http://SERVER_IP/
ssh -i ~/.ssh/id_ed25519_droplet -o IdentitiesOnly=yes deploy@SERVER_IP
```

`curl` should return HTTP response headers from Apache. The SSH command should log in.

**If it goes wrong.** If the SSH session dies, use the Droplet Console:

```bash
sudo ufw disable
sudo ufw allow OpenSSH
sudo ufw enable
sudo ufw status verbose
```

If `ufw allow OpenSSH` says the profile is missing, list profiles and allow the port:

```bash
sudo ufw app list
sudo ufw allow 22/tcp comment 'SSH'
```

If `comment` is rejected, rerun the allow commands without the `comment` clause. If enable says the firewall is already active, check `sudo ufw status verbose` and confirm 22, 80, and 443 before changing anything else. If `curl` to `127.0.0.1` on the droplet works and `curl` from your computer does not, check the DigitalOcean Cloud Firewall attached to the droplet, if there is one. That firewall is separate from UFW.

### Results

<!-- Write what you actually saw. -->

## 5. Turn on unattended-upgrades

**Why.** Security updates should install on a schedule after this lab, without another manual apt session.

**Commands.** On the droplet. `/etc/apt/apt.conf.d/20auto-upgrades` is the on/off switch. This lab does not change `Unattended-Upgrade::Automatic-Reboot`.

```bash
sudo apt-get update
sudo apt-get install -y unattended-upgrades
printf '%s\n' \
  'APT::Periodic::Update-Package-Lists "1";' \
  'APT::Periodic::Unattended-Upgrade "1";' \
  | sudo tee /etc/apt/apt.conf.d/20auto-upgrades >/dev/null
sudo systemctl enable unattended-upgrades.service
sudo systemctl enable --now apt-daily.timer apt-daily-upgrade.timer
grep -n 'Automatic-Reboot' /etc/apt/apt.conf.d/50unattended-upgrades
```

Record the `Automatic-Reboot` line you see, including whether it is commented out. The dry run contacts the Ubuntu mirrors, can take a few minutes, and does not install packages. The timers use a random delay, so an upgrade may happen later rather than during this step.

```bash
sudo unattended-upgrades --dry-run
echo "exit=$?"
```

**Verify.**

```bash
cat /etc/apt/apt.conf.d/20auto-upgrades
systemctl is-enabled apt-daily.timer apt-daily-upgrade.timer
systemctl list-timers apt-daily.timer apt-daily-upgrade.timer
```

The file should contain `Update-Package-Lists "1"` and `Unattended-Upgrade "1"`. Both timers should be enabled. Record the next run times from the timer list.

**If it goes wrong.** If `systemctl enable unattended-upgrades.service` says the unit is static, leave it. The timers and `20auto-upgrades` are the switch. To turn automatic installs off:

```bash
printf '%s\n' \
  'APT::Periodic::Update-Package-Lists "0";' \
  'APT::Periodic::Unattended-Upgrade "0";' \
  | sudo tee /etc/apt/apt.conf.d/20auto-upgrades >/dev/null
```

If the dry run exits non-zero, record the error from `/var/log/unattended-upgrades/unattended-upgrades.log`. A mirror failure here leaves the SSH and UFW changes as they are. If apt stops to ask about a configuration file you have not edited, take the package maintainer's version.

### Results

<!-- Write what you actually saw. -->

## 6. Update Apache and hide version details

**Why.** The version in the `Server` header and on generated error pages tells a scanner which bugs to try.

**Commands.** On the droplet. This upgrades `apache2` when the candidate is newer. It does not replace `/var/www/html/index.html`.

```bash
sudo apt-get update
apt-cache policy apache2
sudo apt-get install --only-upgrade -y apache2
apache2 -v
grep -n -E 'ServerTokens|ServerSignature' /etc/apache2/conf-enabled/*.conf
```

Record the installed and candidate versions. The packaged `security.conf` on Ubuntu sets `ServerTokens OS` and `ServerSignature On`. Confirm the lines you actually have. Apache keeps the last value it reads, and `conf-enabled` is included in lexical order. `zzz-server-tokens.conf` sorts after `security.conf`.

```bash
sudo tee /etc/apache2/conf-available/zzz-server-tokens.conf >/dev/null <<'EOF'
ServerTokens Prod
ServerSignature Off
EOF
sudo a2enconf zzz-server-tokens
sudo apache2ctl configtest
sudo systemctl reload apache2
```

Reload only if `configtest` prints `Syntax OK` and exits 0.

**Verify.**

```bash
curl -sI http://127.0.0.1/
curl -s http://127.0.0.1/no-such-hardening-lab-page
systemctl is-active apache2
```

Apache defines `ServerTokens Prod` as the product name only, so the `Server` header should be `Apache`, with no version and no OS token. On the stock error page, the body of the missing URL should have no version line. If you replaced Apache's error documents, use the `Server` header. Also fetch `/` and confirm the body is still your `index.html`.

From your computer, `curl -sI http://SERVER_IP/` should show the same `Server` header.

**If it goes wrong.**

```bash
sudo a2disconf zzz-server-tokens
sudo apache2ctl configtest && sudo systemctl reload apache2
```

If Apache is down:

```bash
systemctl status apache2 --no-pager
sudo journalctl -u apache2 -n 40 --no-pager
```

If the header still contains a version, a later file is winning:

```bash
grep -n -E 'ServerTokens|ServerSignature' -r /etc/apache2/conf-enabled /etc/apache2/sites-enabled /etc/apache2/apache2.conf
```

`ServerTokens Prod` still sends the word `Apache`.

### Results

<!-- Write what you actually saw. -->

## 7. Optional: HTTPS with Let's Encrypt

Skip this step if you do not have a domain name. This lab uses an HTTP-01 certificate for a DNS name pointed at the droplet. It does not cover a certificate for a bare IP address.

**Why.** On port 80 the page is readable on the path between the visitor and the droplet.

**Commands.** On the droplet, compare DNS with this host. Use your domain in place of `example.com`.

```bash
getent ahosts example.com
ip -4 -br addr show
```

If `getent` does not show an address that is on this droplet, stop and fix DNS before installing Certbot. From your computer, this should reach Apache:

```bash
curl -sI http://example.com/
```

Save the vhosts before Certbot edits them:

```bash
sudo cp -a /etc/apache2/sites-available /root/apache-sites-available.bak
sudo cp -a /etc/apache2/sites-enabled /root/apache-sites-enabled.bak
```

Current Ubuntu server docs install Certbot from snap. The snap includes the Apache plugin. Removing an apt `certbot` avoids running an older binary. `apt-get remove` of a package that is not installed exits without changing anything.

```bash
sudo apt-get remove -y certbot
sudo snap install --classic certbot
sudo ln -sf /snap/bin/certbot /usr/local/bin/certbot
certbot --version
```

The first `snap install` can sit for a minute while `snapd` starts. Add `-d www.example.com` only if that name also resolves to this droplet. Port 80 has to stay open. UFW already allows it.

```bash
sudo certbot --apache -d example.com
```

Certbot asks for an email address, agreement to the Let's Encrypt terms, whether the EFF may email you, and whether to redirect HTTP to HTTPS. Choose redirect if you want port 80 to send visitors to HTTPS. After it finishes, open the new `*-le-ssl.conf` in `/etc/apache2/sites-enabled/` and confirm `DocumentRoot` is the directory that holds your `index.html`. The packaged default is `/var/www/html`.

**Verify.**

```bash
sudo apache2ctl configtest
sudo certbot certificates
curl -sI https://example.com/
curl -sI http://example.com/
systemctl list-timers --all | grep certbot
sudo certbot renew --dry-run
echo "exit=$?"
```

`configtest` should print `Syntax OK`. The HTTPS response should be your site, and the `Server` header should still have no version. If you chose redirect, the HTTP request should be a redirect to HTTPS. The timer list should include `snap.certbot.renew.timer`. The dry run uses Let's Encrypt staging. Record its exit status.

**If it goes wrong.** If DNS was wrong, Certbot fails and port 80 should still serve the old site. If `apache2ctl configtest` fails after Certbot, put the saved vhosts back. This chain stops at the first failure. If either backup directory is missing, `rm` does not run.

```bash
sudo test -d /root/apache-sites-available.bak \
  && sudo test -d /root/apache-sites-enabled.bak \
  && sudo rm -rf /etc/apache2/sites-available /etc/apache2/sites-enabled \
  && sudo cp -a /root/apache-sites-available.bak /etc/apache2/sites-available \
  && sudo cp -a /root/apache-sites-enabled.bak /etc/apache2/sites-enabled \
  && sudo apache2ctl configtest \
  && sudo systemctl reload apache2
```

If `snap` is not installed, `sudo apt-get install -y snapd` and rerun the snap commands. If the laptop can reach the droplet by IP and `http://example.com/` times out, check the A record and any DigitalOcean Cloud Firewall. HTTP-01 needs port 80 open from the internet.

### Results

<!-- Write what you actually saw. -->
