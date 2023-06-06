#!/bin/sh

(>&2 echo "Remediating: 'xccdf_org.ssgproject.content_rule_harden_sshd_macs_openssh_conf_crypto_policy'")

sshd_approved_macs='hmac-sha2-512,hmac-sha2-256'


if [ -e "/etc/crypto-policies/back-ends/openssh.config" ] ; then
    
    LC_ALL=C sed --follow-symlinks -i "/^.*MACs\s\+/d" "/etc/crypto-policies/back-ends/openssh.config"
else
    touch "/etc/crypto-policies/back-ends/openssh.config"
fi
# make sure file has newline at the end
sed --follow-symlinks -i -e '$a\' "/etc/crypto-policies/back-ends/openssh.config"

cp "/etc/crypto-policies/back-ends/openssh.config" "/etc/crypto-policies/back-ends/openssh.config.bak"
# Insert at the end of the file
printf '%s\n' "MACs ${sshd_approved_macs}" >> "/etc/crypto-policies/back-ends/openssh.config"
# Clean up after ourselves.
rm "/etc/crypto-policies/back-ends/openssh.config.bak"
