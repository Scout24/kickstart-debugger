kickstart-debugger
==================

Debug tool for kickstart installations. Start a web server in %pre script stage that allows debugging the kickstart process while it happens via a simple web GUI.

Installation
------------

1. Put the [kickstart-debugger.py](kickstart-debugger/tree/master/kickstart-debugger.py) script onto a web server of your choice.
1. Add the following code to the `%pre` section of your kickstart script:

    ```bash
    # Initialize kickstart debug webserver. /dev is also available from within the chrooted post script :-)
    wget -O- -q http://<your webserver>/kickstart-debugger.py | python - -p 80 >/tmp/access.log 2>&1 &
    ```
1. Kickstart a server and observe the process through the  web GUI.

Customization
-------------

The `/dev` path is shared between  the installation system and the `%post` script running chrooted in the installed system. That allows us to use this path as an data exchange directory between code failing in the `%post` script and the kickstart debugger running outside the chroot.

The kickstart debugger will display the content of a `/dev/kickstart_debugger_error.txt` file in large red on the main page if this file exists. Our `%post` scripts use this to communicate known error situations to the user with the help of this bash function:

```bash
die() { 
    echo "ERROR $@" 1>&2 
	echo "$@" >/dev/kickstart_debugger_error.txt
	exit 1
}
```

The following function that installs a package via yum with retries illustrates the usage:
```bash
yum_install_with_retry() {
    local packages=("$@")
	local timeout=600 sleep_delay=31 mystart=$SECONDS
	while res=$(yum install -y "${packages[@]}" 2>&1) ; ! rpm -q "${packages[@]}" ; do
		if (( SECONDS > mystart + timeout )) ; then 
			die "Could not yum install ${packages[@]}:<br/><pre>$res</pre>"
		fi			
		yum clean all
		sleep $sleep_delay
	done
}
```

Notes
-----

This is my first real python project, please forgive the style and help me with pull requests.
Schlomo