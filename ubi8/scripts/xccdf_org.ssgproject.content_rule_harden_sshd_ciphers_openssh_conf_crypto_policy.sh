#!/bin/sh

(>&2 echo "Remediating: 'xccdf_org.ssgproject.content_rule_harden_sshd_ciphers_openssh_conf_crypto_policy'")

sshd_approved_ciphers='aes256-ctr,aes192-ctr,aes128-ctr'


if [ -e "/etc/crypto-policies/back-ends/openssh.config" ] ; then
    
    LC_ALL=C sed --follow-symlinks -i "/^.*Ciphers\s\+/d" "/etc/crypto-policies/back-ends/openssh.config"
else
    touch "/etc/crypto-policies/back-ends/openssh.config"
fi
# make sure file has newline at the end
sed --follow-symlinks -i -e '$a\' "/etc/crypto-policies/back-ends/openssh.config"

cp "/etc/crypto-policies/back-ends/openssh.config" "/etc/crypto-policies/back-ends/openssh.config.bak"
# Insert at the end of the file
printf '%s\n' "Ciphers ${sshd_approved_ciphers}" >> "/etc/crypto-policies/back-ends/openssh.config"
# Clean up after ourselves.
rm "/etc/crypto-policies/back-ends/openssh.config.bak"
