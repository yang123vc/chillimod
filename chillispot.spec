Summary:   ChilliSpot is a Wireless LAN Access Point Controller
Name:      chillispot
Version:   1.1.0
Release:   1
URL:       http://www.chillispot.org
Source0:   %{name}-%{version}.tar.gz
License:   GPL
Group:     System Environment/Daemons
BuildRoot: %{_tmppath}/%{name}-root

%description 

ChilliSpot is an open source captive portal or wireless LAN access point
controller. It supports web based login which is today's standard for
public HotSpots and it supports Wireless Protected Access (WPA) which
is the standard of the future. Authentication, Authorization and 
Accounting (AAA) is handled by your favorite radius server. Read more
on http://www.chillispot.org

%prep
%setup -q

%build

./configure --prefix=/usr --enable-static-exec

make

%install

make install prefix=$RPM_BUILD_ROOT/usr
strip $RPM_BUILD_ROOT/usr/sbin/chilli

#Copy chilli init script in place
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m755 doc/chilli.init \
	$RPM_BUILD_ROOT/etc/rc.d/init.d/chilli

#Copy chilli.conf in place
install -m755 doc/chilli.conf \
	$RPM_BUILD_ROOT/etc/chilli.conf

#Clean up unwanted library files
rm -rf $RPM_BUILD_ROOT/usr/include/*
rm -rf $RPM_BUILD_ROOT/usr/lib/*


%clean
rm -rf $RPM_BUILD_ROOT
make clean

%post
/sbin/chkconfig --add chilli

%files
%defattr(-,root,root)

%attr(755, root, root) /usr/sbin/chilli
%attr(755, root, root) /etc/rc.d/init.d/chilli

%doc doc/chilli.conf
%doc doc/chilli.init
%doc doc/firewall.iptables
%doc doc/hotspotlogin.cgi
%doc doc/dictionary.chillispot
%doc COPYING

%doc /usr/man/man8/chilli.8.gz

%config /etc/chilli.conf


%changelog
* Thu Mar 25 2004  <support@chillispot.org>
- Initial release.
