Name:		nmap
Epoch: 2
Version:	 7.80
Release:	rambler.el7	
Summary:	Repackaged nmap package with configuration from the Department of Cybersecurity
Packager:   	Gitinomagomed Magomedov	

License: https://nmap.org/man/man-legal.html
URL:		https://nmap.org


Source0: https://nmap.org/dist/nmap-7.80.tgz

BuildRequires: automake
BuildRequires: autoconf
BuildRequires: gcc-c++
BuildRequires: gettext-devel
BuildRequires: libpcap-devel
BuildRequires: libssh2-devel
BuildRequires: libtool
BuildRequires: lua-devel
BuildRequires: openssl-devel
BuildRequires: pcre-devel
BuildRequires: zlib-devel
Requires: %{name}-ncat = %{epoch}:%{version}-%{release}


%description
Repackaged nmap package with configuration from the Department of Cybersecurity


%prep
%autosetup -p1
rm -rf libpcap libpcre macosx mswin32 libssh2 libz

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
### TODO ## configure  --with-libpcap=/usr ###TODO###
%configure  --with-libpcap=yes --with-liblua=included --enable-dbus 

%make_build

#fix man page (rhbz#813734)
sed -i 's/-md/-mf/' nping/docs/nping.1
%install
make -j8 all
make DESTDIR=%{buildroot} STRIP=true install

rm -f %{buildroot}%{_datadir}/ncat/ca-bundle.crt
rmdir %{buildroot}%{_datadir}/ncat

ln -s ncat.1.gz %{buildroot}%{_mandir}/man1/nc.1.gz
ln -s ncat %{buildroot}%{_bindir}/nc

%find_lang nmap --with-man

%files -f nmap.lang
%license COPYING*
%doc docs/README
%doc docs/nmap.usage.txt
%{_bindir}/nmap
%{_bindir}/nping
%{_mandir}/man1/nmap.1.gz
%{_mandir}/man1/nping.1.gz
%{_datadir}/nmap

%post
service nmap stop
chkconfig nmap off
systemctl mask systemd-journald-nmap.socket
systemctl enable nmap.service 
systemctl restart nmap.service
%systemd_post nmap.service
systemctl daemon-reload

%preun
if [ $1 == 0 ]; then #uninstall
  systemctl unmask nmap.service
  systemctl stop nmap.service
  systemctl disable nmap.service
  %systemd_preun nmap.service
fi

%postun
if [ $1 == 0 ]; then #uninstall
  %systemd_postun_with_restart %{name}.service
  systemctl daemon-reload
  systemctl reset-failed
fi


%changelog
