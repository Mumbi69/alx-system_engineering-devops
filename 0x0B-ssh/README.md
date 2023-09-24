# SSH
* SSH is a secure protocol used as the primary means of connecting to Linux servers remotely.
* It provides a text-based interface by spawning a remote shell.
* SSH is the client
* SSHD is the server (Open SSH Daemon)
* To genrate keys run this command:
> > > * ssh-keygen
> > > * ~/.ssh/id_rsa(private key)
> > > * ~/.ssh/id_rsa.pub(public key)
* Public key goes into server 'authorized_keys' file
