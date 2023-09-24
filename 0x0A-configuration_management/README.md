# Configuration management
* The file type can manage normal files, directories, and symlinks; the type should be specified in the ensure attribute.
* File contents can be managed directly with the content attribute, or downloaded from a remote source using the source attribute;  
* file { 'resource title':
*  path                    => # (namevar) The path to the file to manage.  Must be fully qualified.
*  ensure                  => # Whether the file should exist, and if so what kind of file it should be. Possible values are present, absent, file, directory, and link.
*  backup                  => # Whether (and how) file content should be backed up before being replaced.
*  checksum                => # The checksum type to use when determining whether to replace a file’s contents. The default checksum type is md5.
*  checksum_value          => # The checksum of the source contents. Only md5 , sha256, sha224, sha384 and sha512 are supported when specifying this parameter.
*  content                 => # The desired contents of a file, as a string. This attribute is mutually exclusive with source and target.
*  ctime                   => # A read-only state to check the file ctime. On most modern *nix-like systems, this is the time of the most recent change to the owner, group, permissions, or content of the file.
*  force                   => # Perform the file operation even if it will destroy one or more directories.
*  group                   => # Which group should own the file.  Argument can can be either a group name or a group ID.
*  ignore                  => # A parameter which omits action on files matching specified patterns during recursion.
*  links                   => # How to handle links during file actions.  During file copying, follow will copy the target file instead of the link and manage will copy the link itself.
*  mode                    => # The desired permissions mode for the file, in symbolic or numeric notation.
*  mtime                   => # A read-only state to check the file mtime. On *nix-like systems, this is the time of the most recent change to the content of the file.
*  owner                   => # The user to whom the file should belong. Argument can be a user name or a user ID.
*  provider                => # The specific backend to use for this `file resource. 
*  purge                   => # Whether unmanaged files should be purged. This option only makes sense when ensure => directory and recurse => true.
*  recurse                 => # Whether to recursively manage the _contents_ of a directory.
*  recurselimit            => # How far Puppet should descend into subdirectories, when using ensure => directory and either recurse => true or recurse => remote.
*  replace                 => # Whether to replace a file or symlink that already exists on the local system but whose content doesn’t match what the source or content attribute specifies.
*  selinux_ignore_defaults => # If this is set then Puppet will not ask SELinux  (via matchpathcon) to supply defaults for the SELinux attributes (seluser, selrole, seltype, and selrange).
*  selrange                => # What the SELinux range component of the context of the file should be.
*  selrole                 => # What the SELinux role component of the context of the file should be.
*  seltype                 => # What the SELinux type component of the context of the file should be.
*  seluser                 => # What the SELinux user component of the context of the file should be.
*  show_diff               => # Whether to display differences when the file changes, defaulting to true.
*  source                  => # A source file, which will be copied into place on the local system.
*  source_permissions      => # Whether (and how) Puppet should copy owner , group, and mode permissions from the source to file resources when the permissions are not explicitly specified.
*  sourceselect            => # Whether to copy all valid sources, or just the first one.
*  target                  => # The target for creating a link.  Currently , symlinks are the only type supported. This attribute is mutually exclusive with source and content.
*  type                    => # A read-only state to check the file type.
*  validate_cmd            => # A command for validating the file's syntax before replacing it.
*  validate_replacement    => # The replacement string in a `validate_cmd` that will be replaced with an input file name.
}
