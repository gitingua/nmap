
%global _hardened_build 1

Name: nmap
Epoch: 2
Version: 7.80
#global prerelease TEST5
Release: 6%{?dist}
Summary: Network exploration tool and security scanner
URL: http://nmap.org/
# Uses combination of licenses based on GPL license, but with extra modification
# so it got its own license tag rhbz#1055861
License: Nmap

Source0: http://nmap.org/dist/%{name}-%{version}%{?prerelease}.tar.bz2

#prevent possible race condition for shtool, rhbz#158996
Patch1: nmap-4.03-mktemp.patch

#don't suggest to scan microsoft
Patch2: nmap-4.52-noms.patch

# upstream provided patch for rhbz#845005, not yet in upstream repository
Patch3: ncat_reg_stdin.diff
Patch4: nmap-6.25-displayerror.patch
# https://github.com/nmap/nmap/commit/33f421fd6e68fcb8ed50071661d9704717c81b2b.patch
Patch5: nmap-unsolicited_arp_assert.patch

BuildRequires: automake
BuildRequires: autoconf
BuildRequires: gcc-c++
BuildRequires: gettext-devel
BuildRequires: libpcap-devel
%if 0%{?fedora} 
BuildRequires: libssh2-devel
%endif
BuildRequires: libtool
BuildRequires: lua-devel
BuildRequires: openssl-devel
BuildRequires: pcre-devel
BuildRequires: zlib-devel
Requires: %{name}-ncat = %{epoch}:%{version}-%{release}

Obsoletes: nmap-frontend
Obsoletes: nmap-ndiff

%define pixmap_srcdir zenmap/share/pixmaps

%description
Nmap is a utility for network exploration or security auditing.  It supports
ping scanning (determine which hosts are up), many port scanning techniques
(determine what services the hosts are offering), and TCP/IP fingerprinting
(remote host operating system identification). Nmap also offers flexible target
and port specification, decoy scanning, determination of TCP sequence
predictability characteristics, reverse-identd scanning, and more. In addition
to the classic command-line nmap executable, the Nmap suite includes a flexible
data transfer, redirection, and debugging tool (netcat utility ncat), a utility
for comparing scan results (ndiff), and a packet generation and response
analysis tool (nping). 

%package ncat
Summary: Nmap's Netcat replacement
Obsoletes: nc < 1.109.20120711-2
Obsoletes: nc6 < 1.00-22
Provides: nc nc6

%description ncat
Ncat is a feature packed networking utility which will read and
write data across a network from the command line.  It uses both
TCP and UDP for communication and is designed to be a reliable
back-end tool to instantly provide network connectivity to other
applications and users. Ncat will not only work with IPv4 and IPv6
but provides the user with a virtually limitless number of potential
uses.


%prep
%autosetup -p1

#be sure we're not using tarballed copies of some libraries
#rm -rf liblua libpcap libpcre macosx mswin32 ###TODO###

rm -rf libpcap libpcre macosx mswin32 libssh2 libz

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
### TODO ## configure  --with-libpcap=/usr ###TODO###
%configure  --with-libpcap=yes --with-liblua=included \
  --without-zenmap --without-ndiff \
%if 0%{?fedora} 
  --with-libssh2=yes  \
%else
  --with-libssh2=no  \
%endif
  --enable-dbus 

%make_build

#fix man page (rhbz#813734)
sed -i 's/-md/-mf/' nping/docs/nping.1

%install
#prevent stripping - replace strip command with 'true'
make DESTDIR=%{buildroot} STRIP=true install

#do not include certificate bundle (#734389)
rm -f %{buildroot}%{_datadir}/ncat/ca-bundle.crt
rmdir %{buildroot}%{_datadir}/ncat

#we provide 'nc' replacement
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

%files ncat 
%license COPYING
%doc ncat/docs/AUTHORS ncat/docs/README ncat/docs/THANKS ncat/docs/examples
%{_bindir}/nc
%{_bindir}/ncat
%{_mandir}/man1/nc.1.gz
%{_mandir}/man1/ncat.1.gz
