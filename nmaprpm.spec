Name:		nmap
Epoch: 2
Version:	 7.80
Release:	rambler.el7	
Summary:	Repackaged nmap package with configuration from the Department of Cybersecurity
Packager:   	Gitinomagomed Magomedov	
%global full_name nmap-7.80

License: https://nmap.org/man/man-legal.html
URL:		https://nmap.org

Source0:https://nmap.org/dist/nmap-7.80.tgz

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

%configure  --with-libpcap=yes --with-liblua=included --enable-dbus


sed -i 's/-md/-mf/' nping/docs/nping.1
%install
make -j8 all
make DESTDIR=%{buildroot} STRIP=true install

#do not include certificate bundle (#734389)
rm -f %{buildroot}%{_datadir}/ncat/ca-bundle.crt
rmdir %{buildroot}%{_datadir}/ncat

#we provide 'nc' replacement
ln -s ncat.1.gz %{buildroot}%{_mandir}/man1/nc.1.gz
ln -s ncat %{buildroot}%{_bindir}/nc

install -m 0755 /usr/bin/ncat	%{buildroot}/usr/bin/ncat
install -m 0755 /usr/bin/ndiff	%{buildroot}/usr/bin/ndiff
install -m 0755 /usr/bin/nmap	%{buildroot}/usr/bin/nmap
#install -m 0755 /root/rpmbuild/BUILD/nmap-7.80/nmap-update	%{buildroot}/usr/bin/nmap-update
install -m 0755 /opt/nmap/usr/local/bin/nmapfe	%{buildroot}/usr/bin/nmapfe
install -m 0755 /usr/bin/nping	%{buildroot}/usr/bin/nping
install -m 0755 /opt/nmap/usr/local/bin/uninstall_ndiff	%{buildroot}/usr/bin/uninstall_ndiff
install -m 0755 /opt/nmap/usr/local/bin/uninstall_zenmap	%{buildroot}/usr/bin/uninstall_zenmap
install -m 0755 /opt/nmap/usr/local/bin/xnmap	%{buildroot}/usr/bin/xnmap
install -m 0755 /opt/nmap/usr/local/bin/zenmap	%{buildroot}/usr/bin/zenmap
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/ndiff.py	%{buildroot}/usr/lib/python2.7/site-packages/ndiff.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/ndiff.pyc	%{buildroot}/usr/lib/python2.7/site-packages/ndiff.pyc
install -m 0755 /usr/lib/python2.6/site-packages/ndiff.pyo	%{buildroot}/usr/lib/python2.7/site-packages/ndiff.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/__init__.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/__init__.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/__init__.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/__init__.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/__init__.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/__init__.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/boxes.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/boxes.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/boxes.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/buttons.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/buttons.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/buttons.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/comboboxes.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/comboboxes.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/comboboxes.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/expanders.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/expanders.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/expanders.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/frames.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/frames.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/frames.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/labels.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/labels.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/labels.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/textview.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/textview.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/textview.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/windows.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/windows.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/bestwidgets/windows.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/ArgvHandle.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/ArgvHandle.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/ArgvHandle.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/Coordinate.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/Coordinate.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/Coordinate.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/Graph.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/Graph.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/Graph.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/Info.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/Info.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/Info.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/Interpolation.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/Interpolation.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/Interpolation.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/XMLHandler.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/XMLHandler.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/XMLHandler.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/__init__.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/__init__.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/core/__init__.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/Application.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/Application.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/Application.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/ControlWidget.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/ControlWidget.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/ControlWidget.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/Dialogs.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/Dialogs.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/Dialogs.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/HostsViewer.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/HostsViewer.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/HostsViewer.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/Image.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/Image.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/Image.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/LegendWindow.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/LegendWindow.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/LegendWindow.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/NodeNotebook.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/NodeNotebook.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/NodeNotebook.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/NodeWindow.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/NodeWindow.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/NodeWindow.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/RadialNet.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/RadialNet.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/RadialNet.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/SaveDialog.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/SaveDialog.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/SaveDialog.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/Toolbar.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/Toolbar.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/Toolbar.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/__init__.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/__init__.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/gui/__init__.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/util/__init__.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/util/__init__.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/util/__init__.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/util/drawing.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/util/drawing.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/util/drawing.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/util/geometry.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/util/geometry.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/util/geometry.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/util/integration.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/util/integration.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/util/integration.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/util/misc.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/util/misc.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/radialnet/util/misc.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmap-7.80-py2.7.egg-info
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/BasePaths.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/BasePaths.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/BasePaths.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/DelayedObject.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/DelayedObject.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/DelayedObject.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/Diff.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/Diff.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/Diff.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/I18N.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/I18N.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/I18N.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/NSEDocParser.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/NSEDocParser.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/NSEDocParser.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/Name.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/Name.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/Name.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/NetworkInventory.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/NetworkInventory.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/NetworkInventory.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/NmapCommand.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/NmapCommand.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/NmapCommand.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/NmapOptions.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/NmapOptions.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/NmapOptions.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/NmapParser.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/NmapParser.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/NmapParser.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/Paths.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/Paths.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/Paths.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/RecentScans.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/RecentScans.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/RecentScans.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/ScriptArgsParser.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/ScriptArgsParser.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/ScriptArgsParser.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/ScriptMetadata.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/ScriptMetadata.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/ScriptMetadata.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/SearchResult.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/SearchResult.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/SearchResult.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/StringPool.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/StringPool.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/StringPool.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/TargetList.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/TargetList.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/TargetList.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/UmitConf.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/UmitConf.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/UmitConf.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/UmitConfigParser.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/UmitConfigParser.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/UmitConfigParser.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/UmitDB.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/UmitDB.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/UmitDB.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/UmitLogging.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/UmitLogging.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/UmitLogging.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/UmitOptionParser.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/UmitOptionParser.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/UmitOptionParser.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/Version.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/Version.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/Version.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/__init__.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/__init__.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapCore/__init__.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/About.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/About.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/About.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/App.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/App.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/App.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/BugReport.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/BugReport.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/BugReport.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/CrashReport.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/CrashReport.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/CrashReport.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/DiffCompare.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/DiffCompare.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/DiffCompare.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/FileChoosers.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/FileChoosers.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/FileChoosers.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/FilterBar.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/FilterBar.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/FilterBar.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/Icons.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/Icons.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/Icons.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/MainWindow.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/MainWindow.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/MainWindow.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/NmapOutputProperties.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/NmapOutputProperties.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/NmapOutputProperties.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/NmapOutputViewer.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/NmapOutputViewer.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/NmapOutputViewer.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/OptionBuilder.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/OptionBuilder.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/OptionBuilder.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/Print.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/Print.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/Print.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ProfileCombo.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ProfileCombo.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ProfileCombo.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ProfileEditor.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ProfileEditor.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ProfileEditor.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ProfileHelp.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ProfileHelp.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ProfileHelp.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanHostDetailsPage.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanHostDetailsPage.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanHostDetailsPage.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanHostsView.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanHostsView.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanHostsView.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanInterface.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanInterface.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanInterface.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanNmapOutputPage.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanNmapOutputPage.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanNmapOutputPage.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanOpenPortsPage.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanOpenPortsPage.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanOpenPortsPage.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanRunDetailsPage.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanRunDetailsPage.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanRunDetailsPage.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanScanListPage.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanScanListPage.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanScanListPage.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanToolbar.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanToolbar.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScanToolbar.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScansListStore.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScansListStore.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScansListStore.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScriptInterface.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScriptInterface.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/ScriptInterface.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/SearchGUI.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/SearchGUI.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/SearchGUI.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/SearchWindow.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/SearchWindow.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/SearchWindow.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/TargetCombo.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/TargetCombo.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/TargetCombo.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/TopologyPage.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/TopologyPage.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/TopologyPage.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/__init__.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/__init__.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/__init__.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/__init__.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/__init__.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/__init__.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/gtkutils.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/gtkutils.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/gtkutils.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higboxes.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higboxes.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higboxes.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higbuttons.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higbuttons.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higbuttons.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higdialogs.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higdialogs.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higdialogs.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higentries.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higentries.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higentries.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higexpanders.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higexpanders.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higexpanders.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higframe.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higframe.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higframe.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higlabels.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higlabels.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higlabels.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higlogindialogs.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higlogindialogs.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higlogindialogs.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/hignotebooks.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/hignotebooks.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/hignotebooks.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higprogressbars.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higprogressbars.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higprogressbars.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higscrollers.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higscrollers.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higscrollers.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higspinner.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higspinner.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higspinner.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higtables.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higtables.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higtables.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higtextviewers.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higtextviewers.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higtextviewers.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higwindows.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higwindows.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/higwindows.pyo
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/utils.py
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/utils.pyc
install -m 0755 /opt/nmap/usr/local/lib/python2.7/site-packages/zenmapGUI/higwidgets/utils.pyo
install -m 0755 /opt/nmap/usr/local/share/applications/zenmap-root.desktop	%{buildroot}/usr/share/applications/zenmap-root.desktop
install -m 0755 /opt/nmap/usr/local/share/applications/zenmap.desktop	%{buildroot}/usr/share/applications/zenmap.desktop
install -m 0755 /usr/share/man/de/man1/nmap.1.gz	%{buildroot}/usr/share/man/de/man1/nmap.1.gz
install -m 0755 /usr/share/man/es/man1/nmap.1.gz	%{buildroot}/usr/share/man/es/man1/nmap.1.gz
install -m 0755 /usr/share/man/fr/man1/nmap.1.gz	%{buildroot}/usr/share/man/fr/man1/nmap.1.gz
install -m 0755 /usr/share/man/hr/man1/nmap.1.gz	%{buildroot}/usr/share/man/hr/man1/nmap.1.gz
install -m 0755 /usr/share/man/hu/man1/nmap.1.gz	%{buildroot}/usr/share/man/hu/man1/nmap.1.gz
install -m 0755 /usr/share/man/it/man1/nmap.1.gz	%{buildroot}/usr/share/man/it/man1/nmap.1.gz
install -m 0755 /usr/share/man/ja/man1/nmap.1.gz	%{buildroot}/usr/share/man/ja/man1/nmap.1.gz
install -m 0755 /usr/share/man/man1/ncat.1.gz	%{buildroot}/usr/share/man/man1/ncat.1.gz
install -m 0755 /usr/share/man/man1/ndiff.1.gz	%{buildroot}/usr/share/man/man1/ndiff.1.gz
install -m 0755 /usr/share/man/man1/nmap-update.1.gz	%{buildroot}/usr/share/man/man1/nmap-update.1.gz
install -m 0755 /usr/share/man/man1/nmap.1.gz	%{buildroot}/usr/share/man/man1/nmap.1.gz
install -m 0755 /usr/share/man/man1/nping.1.gz	%{buildroot}/usr/share/man/man1/nping.1.gz
install -m 0755 /usr/share/man/man1/zenmap.1.gz	%{buildroot}/usr/share/man/man1/zenmap.1.gz
install -m 0755 /usr/share/man/pl/man1/nmap.1.gz	%{buildroot}/usr/share/man/pl/man1/nmap.1.gz
install -m 0755 /usr/share/man/pt_BR/man1/nmap.1.gz	%{buildroot}/usr/share/man/pt_BR/man1/nmap.1.gz
install -m 0755 /usr/share/man/pt_PT/man1/nmap.1.gz	%{buildroot}/usr/share/man/pt_PT/man1/nmap.1.gz
install -m 0755 /usr/share/man/ro/man1/nmap.1.gz	%{buildroot}/usr/share/man/ro/man1/nmap.1.gz
install -m 0755 /usr/share/man/ru/man1/nmap.1.gz	%{buildroot}/usr/share/man/ru/man1/nmap.1.gz
install -m 0755 /usr/share/man/sk/man1/nmap.1.gz	%{buildroot}/usr/share/man/sk/man1/nmap.1.gz
install -m 0755 /usr/share/man/zh/man1/nmap.1.gz	%{buildroot}/usr/share/man/zh/man1/nmap.1.gz
install -m 0755 /usr/share/nmap/nmap-mac-prefixes	%{buildroot}/usr/share/nmap/nmap-mac-prefixes
install -m 0755 /usr/share/nmap/nmap-os-db	%{buildroot}/usr/share/nmap/nmap-os-db
install -m 0755 /usr/share/nmap/nmap-payloads	%{buildroot}/usr/share/nmap/nmap-payloads
install -m 0755 /usr/share/nmap/nmap-protocols	%{buildroot}/usr/share/nmap/nmap-protocols
install -m 0755 /usr/share/nmap/nmap-rpc	%{buildroot}/usr/share/nmap/nmap-rpc
install -m 0755 /usr/share/nmap/nmap-service-probes	%{buildroot}/usr/share/nmap/nmap-service-probes
install -m 0755 /usr/share/nmap/nmap-services	%{buildroot}/usr/share/nmap/nmap-services
install -m 0755 /usr/share/nmap/nmap.dtd	%{buildroot}/usr/share/nmap/nmap.dtd
install -m 0755 /usr/share/nmap/nmap.xsl	%{buildroot}/usr/share/nmap/nmap.xsl
install -m 0755 /usr/share/nmap/nse_main.lua	%{buildroot}/usr/share/nmap/nse_main.lua
install -m 0755 /usr/share/nmap/nselib/afp.lua	%{buildroot}/usr/share/nmap/nselib/afp.lua
install -m 0755 /usr/share/nmap/nselib/ajp.lua	%{buildroot}/usr/share/nmap/nselib/ajp.lua
install -m 0755 /usr/share/nmap/nselib/amqp.lua	%{buildroot}/usr/share/nmap/nselib/amqp.lua
install -m 0755 /usr/share/nmap/nselib/anyconnect.lua	%{buildroot}/usr/share/nmap/nselib/anyconnect.lua
install -m 0755 /usr/share/nmap/nselib/asn1.lua	%{buildroot}/usr/share/nmap/nselib/asn1.lua
install -m 0755 /usr/share/nmap/nselib/base32.lua	%{buildroot}/usr/share/nmap/nselib/base32.lua
install -m 0755 /usr/share/nmap/nselib/base64.lua	%{buildroot}/usr/share/nmap/nselib/base64.lua
install -m 0755 /usr/share/nmap/nselib/bin.lua	%{buildroot}/usr/share/nmap/nselib/bin.lua
install -m 0755 /usr/share/nmap/nselib/bitcoin.lua	%{buildroot}/usr/share/nmap/nselib/bitcoin.lua
install -m 0755 /usr/share/nmap/nselib/bits.lua	%{buildroot}/usr/share/nmap/nselib/bits.lua
install -m 0755 /usr/share/nmap/nselib/bittorrent.lua	%{buildroot}/usr/share/nmap/nselib/bittorrent.lua
install -m 0755 /usr/share/nmap/nselib/bjnp.lua	%{buildroot}/usr/share/nmap/nselib/bjnp.lua
install -m 0755 /usr/share/nmap/nselib/brute.lua	%{buildroot}/usr/share/nmap/nselib/brute.lua
install -m 0755 /usr/share/nmap/nselib/cassandra.lua	%{buildroot}/usr/share/nmap/nselib/cassandra.lua
install -m 0755 /usr/share/nmap/nselib/citrixxml.lua	%{buildroot}/usr/share/nmap/nselib/citrixxml.lua
install -m 0755 /usr/share/nmap/nselib/coap.lua	%{buildroot}/usr/share/nmap/nselib/coap.lua
install -m 0755 /usr/share/nmap/nselib/comm.lua	%{buildroot}/usr/share/nmap/nselib/comm.lua
install -m 0755 /usr/share/nmap/nselib/creds.lua	%{buildroot}/usr/share/nmap/nselib/creds.lua
install -m 0755 /usr/share/nmap/nselib/cvs.lua	%{buildroot}/usr/share/nmap/nselib/cvs.lua
install -m 0755 /usr/share/nmap/nselib/data/dns-srv-names	%{buildroot}/usr/share/nmap/nselib/data/dns-srv-names
install -m 0755 /usr/share/nmap/nselib/data/drupal-modules.lst	%{buildroot}/usr/share/nmap/nselib/data/drupal-modules.lst
install -m 0755 /usr/share/nmap/nselib/data/drupal-themes.lst	%{buildroot}/usr/share/nmap/nselib/data/drupal-themes.lst
install -m 0755 /usr/share/nmap/nselib/data/enterprise_numbers.txt	%{buildroot}/usr/share/nmap/nselib/data/enterprise_numbers.txt
install -m 0755 /usr/share/nmap/nselib/data/favicon-db	%{buildroot}/usr/share/nmap/nselib/data/favicon-db
install -m 0755 /usr/share/nmap/nselib/data/http-default-accounts-fingerprints.lua	%{buildroot}/usr/share/nmap/nselib/data/http-default-accounts-fingerprints.lua
install -m 0755 /usr/share/nmap/nselib/data/http-devframework-fingerprints.lua	%{buildroot}/usr/share/nmap/nselib/data/http-devframework-fingerprints.lua
install -m 0755 /usr/share/nmap/nselib/data/http-fingerprints.lua	%{buildroot}/usr/share/nmap/nselib/data/http-fingerprints.lua
install -m 0755 /usr/share/nmap/nselib/data/http-folders.txt	%{buildroot}/usr/share/nmap/nselib/data/http-folders.txt
install -m 0755 /usr/share/nmap/nselib/data/http-sql-errors.lst	%{buildroot}/usr/share/nmap/nselib/data/http-sql-errors.lst
install -m 0755 /usr/share/nmap/nselib/data/http-web-files-extensions.lst	%{buildroot}/usr/share/nmap/nselib/data/http-web-files-extensions.lst
install -m 0755 /usr/share/nmap/nselib/data/idnaMappings.lua	%{buildroot}/usr/share/nmap/nselib/data/idnaMappings.lua
install -m 0755 /usr/share/nmap/nselib/data/ike-fingerprints.lua	%{buildroot}/usr/share/nmap/nselib/data/ike-fingerprints.lua
install -m 0755 /usr/share/nmap/nselib/data/jdwp-class/JDWPExecCmd.class	%{buildroot}/usr/share/nmap/nselib/data/jdwp-class/JDWPExecCmd.class
install -m 0755 /usr/share/nmap/nselib/data/jdwp-class/JDWPExecCmd.java	%{buildroot}/usr/share/nmap/nselib/data/jdwp-class/JDWPExecCmd.java
install -m 0755 /usr/share/nmap/nselib/data/jdwp-class/JDWPSystemInfo.class	%{buildroot}/usr/share/nmap/nselib/data/jdwp-class/JDWPSystemInfo.class
install -m 0755 /usr/share/nmap/nselib/data/jdwp-class/JDWPSystemInfo.java	%{buildroot}/usr/share/nmap/nselib/data/jdwp-class/JDWPSystemInfo.java
install -m 0755 /usr/share/nmap/nselib/data/jdwp-class/README.txt	%{buildroot}/usr/share/nmap/nselib/data/jdwp-class/README.txt
install -m 0755 /usr/share/nmap/nselib/data/mgroupnames.db	%{buildroot}/usr/share/nmap/nselib/data/mgroupnames.db
install -m 0755 /usr/share/nmap/nselib/data/mysql-cis.audit	%{buildroot}/usr/share/nmap/nselib/data/mysql-cis.audit
install -m 0755 /usr/share/nmap/nselib/data/oracle-default-accounts.lst	%{buildroot}/usr/share/nmap/nselib/data/oracle-default-accounts.lst
install -m 0755 /usr/share/nmap/nselib/data/oracle-sids	%{buildroot}/usr/share/nmap/nselib/data/oracle-sids
install -m 0755 /usr/share/nmap/nselib/data/packetdecoders.lua	%{buildroot}/usr/share/nmap/nselib/data/packetdecoders.lua
install -m 0755 /usr/share/nmap/nselib/data/passwords.lst	%{buildroot}/usr/share/nmap/nselib/data/passwords.lst
install -m 0755 /usr/share/nmap/nselib/data/pixel.gif	%{buildroot}/usr/share/nmap/nselib/data/pixel.gif
install -m 0755 /usr/share/nmap/nselib/data/psexec/README	%{buildroot}/usr/share/nmap/nselib/data/psexec/README
install -m 0755 /usr/share/nmap/nselib/data/psexec/backdoor.lua	%{buildroot}/usr/share/nmap/nselib/data/psexec/backdoor.lua
install -m 0755 /usr/share/nmap/nselib/data/psexec/default.lua	%{buildroot}/usr/share/nmap/nselib/data/psexec/default.lua
install -m 0755 /usr/share/nmap/nselib/data/psexec/drives.lua	%{buildroot}/usr/share/nmap/nselib/data/psexec/drives.lua
install -m 0755 /usr/share/nmap/nselib/data/psexec/examples.lua	%{buildroot}/usr/share/nmap/nselib/data/psexec/examples.lua
install -m 0755 /usr/share/nmap/nselib/data/psexec/experimental.lua	%{buildroot}/usr/share/nmap/nselib/data/psexec/experimental.lua
install -m 0755 /usr/share/nmap/nselib/data/psexec/network.lua	%{buildroot}/usr/share/nmap/nselib/data/psexec/network.lua
install -m 0755 /usr/share/nmap/nselib/data/psexec/nmap_service.c	%{buildroot}/usr/share/nmap/nselib/data/psexec/nmap_service.c
install -m 0755 /usr/share/nmap/nselib/data/psexec/nmap_service.vcproj	%{buildroot}/usr/share/nmap/nselib/data/psexec/nmap_service.vcproj
install -m 0755 /usr/share/nmap/nselib/data/psexec/pwdump.lua	%{buildroot}/usr/share/nmap/nselib/data/psexec/pwdump.lua
install -m 0755 /usr/share/nmap/nselib/data/publickeydb	%{buildroot}/usr/share/nmap/nselib/data/publickeydb
install -m 0755 /usr/share/nmap/nselib/data/rtsp-urls.txt	%{buildroot}/usr/share/nmap/nselib/data/rtsp-urls.txt
install -m 0755 /usr/share/nmap/nselib/data/snmpcommunities.lst	%{buildroot}/usr/share/nmap/nselib/data/snmpcommunities.lst
install -m 0755 /usr/share/nmap/nselib/data/ssl-fingerprints	%{buildroot}/usr/share/nmap/nselib/data/ssl-fingerprints
install -m 0755 /usr/share/nmap/nselib/data/targets-ipv6-wordlist	%{buildroot}/usr/share/nmap/nselib/data/targets-ipv6-wordlist
install -m 0755 /usr/share/nmap/nselib/data/tftplist.txt	%{buildroot}/usr/share/nmap/nselib/data/tftplist.txt
install -m 0755 /usr/share/nmap/nselib/data/usernames.lst	%{buildroot}/usr/share/nmap/nselib/data/usernames.lst
install -m 0755 /usr/share/nmap/nselib/data/vhosts-default.lst	%{buildroot}/usr/share/nmap/nselib/data/vhosts-default.lst
install -m 0755 /usr/share/nmap/nselib/data/vhosts-full.lst	%{buildroot}/usr/share/nmap/nselib/data/vhosts-full.lst
install -m 0755 /usr/share/nmap/nselib/data/wp-plugins.lst	%{buildroot}/usr/share/nmap/nselib/data/wp-plugins.lst
install -m 0755 /usr/share/nmap/nselib/data/wp-themes.lst	%{buildroot}/usr/share/nmap/nselib/data/wp-themes.lst
install -m 0755 /usr/share/nmap/nselib/datafiles.lua	%{buildroot}/usr/share/nmap/nselib/datafiles.lua
install -m 0755 /usr/share/nmap/nselib/datetime.lua	%{buildroot}/usr/share/nmap/nselib/datetime.lua
install -m 0755 /usr/share/nmap/nselib/dhcp.lua	%{buildroot}/usr/share/nmap/nselib/dhcp.lua
install -m 0755 /usr/share/nmap/nselib/dhcp6.lua	%{buildroot}/usr/share/nmap/nselib/dhcp6.lua
install -m 0755 /usr/share/nmap/nselib/dns.lua	%{buildroot}/usr/share/nmap/nselib/dns.lua
install -m 0755 /usr/share/nmap/nselib/dnsbl.lua	%{buildroot}/usr/share/nmap/nselib/dnsbl.lua
install -m 0755 /usr/share/nmap/nselib/dnssd.lua	%{buildroot}/usr/share/nmap/nselib/dnssd.lua
install -m 0755 /usr/share/nmap/nselib/drda.lua	%{buildroot}/usr/share/nmap/nselib/drda.lua
install -m 0755 /usr/share/nmap/nselib/eap.lua	%{buildroot}/usr/share/nmap/nselib/eap.lua
install -m 0755 /usr/share/nmap/nselib/eigrp.lua	%{buildroot}/usr/share/nmap/nselib/eigrp.lua
install -m 0755 /usr/share/nmap/nselib/formulas.lua	%{buildroot}/usr/share/nmap/nselib/formulas.lua
install -m 0755 /usr/share/nmap/nselib/ftp.lua	%{buildroot}/usr/share/nmap/nselib/ftp.lua
install -m 0755 /usr/share/nmap/nselib/geoip.lua	%{buildroot}/usr/share/nmap/nselib/geoip.lua
install -m 0755 /usr/share/nmap/nselib/giop.lua	%{buildroot}/usr/share/nmap/nselib/giop.lua
install -m 0755 /usr/share/nmap/nselib/gps.lua	%{buildroot}/usr/share/nmap/nselib/gps.lua
install -m 0755 /usr/share/nmap/nselib/http.lua	%{buildroot}/usr/share/nmap/nselib/http.lua
install -m 0755 /usr/share/nmap/nselib/httpspider.lua	%{buildroot}/usr/share/nmap/nselib/httpspider.lua
install -m 0755 /usr/share/nmap/nselib/iax2.lua	%{buildroot}/usr/share/nmap/nselib/iax2.lua
install -m 0755 /usr/share/nmap/nselib/idna.lua	%{buildroot}/usr/share/nmap/nselib/idna.lua
install -m 0755 /usr/share/nmap/nselib/ike.lua	%{buildroot}/usr/share/nmap/nselib/ike.lua
install -m 0755 /usr/share/nmap/nselib/imap.lua	%{buildroot}/usr/share/nmap/nselib/imap.lua
install -m 0755 /usr/share/nmap/nselib/informix.lua	%{buildroot}/usr/share/nmap/nselib/informix.lua
install -m 0755 /usr/share/nmap/nselib/ipOps.lua	%{buildroot}/usr/share/nmap/nselib/ipOps.lua
install -m 0755 /usr/share/nmap/nselib/ipmi.lua	%{buildroot}/usr/share/nmap/nselib/ipmi.lua
install -m 0755 /usr/share/nmap/nselib/ipp.lua	%{buildroot}/usr/share/nmap/nselib/ipp.lua
install -m 0755 /usr/share/nmap/nselib/irc.lua	%{buildroot}/usr/share/nmap/nselib/irc.lua
install -m 0755 /usr/share/nmap/nselib/iscsi.lua	%{buildroot}/usr/share/nmap/nselib/iscsi.lua
install -m 0755 /usr/share/nmap/nselib/isns.lua	%{buildroot}/usr/share/nmap/nselib/isns.lua
install -m 0755 /usr/share/nmap/nselib/jdwp.lua	%{buildroot}/usr/share/nmap/nselib/jdwp.lua
install -m 0755 /usr/share/nmap/nselib/json.lua	%{buildroot}/usr/share/nmap/nselib/json.lua
install -m 0755 /usr/share/nmap/nselib/knx.lua	%{buildroot}/usr/share/nmap/nselib/knx.lua
install -m 0755 /usr/share/nmap/nselib/ldap.lua	%{buildroot}/usr/share/nmap/nselib/ldap.lua
install -m 0755 /usr/share/nmap/nselib/lfs.luadoc	%{buildroot}/usr/share/nmap/nselib/lfs.luadoc
install -m 0755 /usr/share/nmap/nselib/libssh2-utility.lua	%{buildroot}/usr/share/nmap/nselib/libssh2-utility.lua
install -m 0755 /usr/share/nmap/nselib/libssh2.luadoc	%{buildroot}/usr/share/nmap/nselib/libssh2.luadoc
install -m 0755 /usr/share/nmap/nselib/listop.lua	%{buildroot}/usr/share/nmap/nselib/listop.lua
install -m 0755 /usr/share/nmap/nselib/lpeg-utility.lua	%{buildroot}/usr/share/nmap/nselib/lpeg-utility.lua
install -m 0755 /usr/share/nmap/nselib/lpeg.luadoc	%{buildroot}/usr/share/nmap/nselib/lpeg.luadoc
install -m 0755 /usr/share/nmap/nselib/ls.lua	%{buildroot}/usr/share/nmap/nselib/ls.lua
install -m 0755 /usr/share/nmap/nselib/match.lua	%{buildroot}/usr/share/nmap/nselib/match.lua
install -m 0755 /usr/share/nmap/nselib/membase.lua	%{buildroot}/usr/share/nmap/nselib/membase.lua
install -m 0755 /usr/share/nmap/nselib/mobileme.lua	%{buildroot}/usr/share/nmap/nselib/mobileme.lua
install -m 0755 /usr/share/nmap/nselib/mongodb.lua	%{buildroot}/usr/share/nmap/nselib/mongodb.lua
install -m 0755 /usr/share/nmap/nselib/mqtt.lua	%{buildroot}/usr/share/nmap/nselib/mqtt.lua
install -m 0755 /usr/share/nmap/nselib/msrpc.lua	%{buildroot}/usr/share/nmap/nselib/msrpc.lua
install -m 0755 /usr/share/nmap/nselib/msrpcperformance.lua	%{buildroot}/usr/share/nmap/nselib/msrpcperformance.lua
install -m 0755 /usr/share/nmap/nselib/msrpctypes.lua	%{buildroot}/usr/share/nmap/nselib/msrpctypes.lua
install -m 0755 /usr/share/nmap/nselib/mssql.lua	%{buildroot}/usr/share/nmap/nselib/mssql.lua
install -m 0755 /usr/share/nmap/nselib/multicast.lua	%{buildroot}/usr/share/nmap/nselib/multicast.lua
install -m 0755 /usr/share/nmap/nselib/mysql.lua	%{buildroot}/usr/share/nmap/nselib/mysql.lua
install -m 0755 /usr/share/nmap/nselib/natpmp.lua	%{buildroot}/usr/share/nmap/nselib/natpmp.lua
install -m 0755 /usr/share/nmap/nselib/nbd.lua	%{buildroot}/usr/share/nmap/nselib/nbd.lua
install -m 0755 /usr/share/nmap/nselib/ncp.lua	%{buildroot}/usr/share/nmap/nselib/ncp.lua
install -m 0755 /usr/share/nmap/nselib/ndmp.lua	%{buildroot}/usr/share/nmap/nselib/ndmp.lua
install -m 0755 /usr/share/nmap/nselib/netbios.lua	%{buildroot}/usr/share/nmap/nselib/netbios.lua
install -m 0755 /usr/share/nmap/nselib/nmap.luadoc	%{buildroot}/usr/share/nmap/nselib/nmap.luadoc
install -m 0755 /usr/share/nmap/nselib/nrpc.lua	%{buildroot}/usr/share/nmap/nselib/nrpc.lua
install -m 0755 /usr/share/nmap/nselib/nsedebug.lua	%{buildroot}/usr/share/nmap/nselib/nsedebug.lua
install -m 0755 /usr/share/nmap/nselib/omp2.lua	%{buildroot}/usr/share/nmap/nselib/omp2.lua
install -m 0755 /usr/share/nmap/nselib/oops.lua	%{buildroot}/usr/share/nmap/nselib/oops.lua
install -m 0755 /usr/share/nmap/nselib/openssl.luadoc	%{buildroot}/usr/share/nmap/nselib/openssl.luadoc
install -m 0755 /usr/share/nmap/nselib/ospf.lua	%{buildroot}/usr/share/nmap/nselib/ospf.lua
install -m 0755 /usr/share/nmap/nselib/packet.lua	%{buildroot}/usr/share/nmap/nselib/packet.lua
install -m 0755 /usr/share/nmap/nselib/pcre.luadoc	%{buildroot}/usr/share/nmap/nselib/pcre.luadoc
install -m 0755 /usr/share/nmap/nselib/pgsql.lua	%{buildroot}/usr/share/nmap/nselib/pgsql.lua
install -m 0755 /usr/share/nmap/nselib/pop3.lua	%{buildroot}/usr/share/nmap/nselib/pop3.lua
install -m 0755 /usr/share/nmap/nselib/pppoe.lua	%{buildroot}/usr/share/nmap/nselib/pppoe.lua
install -m 0755 /usr/share/nmap/nselib/proxy.lua	%{buildroot}/usr/share/nmap/nselib/proxy.lua
install -m 0755 /usr/share/nmap/nselib/punycode.lua	%{buildroot}/usr/share/nmap/nselib/punycode.lua
install -m 0755 /usr/share/nmap/nselib/rand.lua	%{buildroot}/usr/share/nmap/nselib/rand.lua
install -m 0755 /usr/share/nmap/nselib/rdp.lua	%{buildroot}/usr/share/nmap/nselib/rdp.lua
install -m 0755 /usr/share/nmap/nselib/re.lua	%{buildroot}/usr/share/nmap/nselib/re.lua
install -m 0755 /usr/share/nmap/nselib/redis.lua	%{buildroot}/usr/share/nmap/nselib/redis.lua
install -m 0755 /usr/share/nmap/nselib/rmi.lua	%{buildroot}/usr/share/nmap/nselib/rmi.lua
install -m 0755 /usr/share/nmap/nselib/rpc.lua	%{buildroot}/usr/share/nmap/nselib/rpc.lua
install -m 0755 /usr/share/nmap/nselib/rpcap.lua	%{buildroot}/usr/share/nmap/nselib/rpcap.lua
install -m 0755 /usr/share/nmap/nselib/rsync.lua	%{buildroot}/usr/share/nmap/nselib/rsync.lua
install -m 0755 /usr/share/nmap/nselib/rtsp.lua	%{buildroot}/usr/share/nmap/nselib/rtsp.lua
install -m 0755 /usr/share/nmap/nselib/sasl.lua	%{buildroot}/usr/share/nmap/nselib/sasl.lua
install -m 0755 /usr/share/nmap/nselib/shortport.lua	%{buildroot}/usr/share/nmap/nselib/shortport.lua
install -m 0755 /usr/share/nmap/nselib/sip.lua	%{buildroot}/usr/share/nmap/nselib/sip.lua
install -m 0755 /usr/share/nmap/nselib/slaxml.lua	%{buildroot}/usr/share/nmap/nselib/slaxml.lua
install -m 0755 /usr/share/nmap/nselib/smb.lua	%{buildroot}/usr/share/nmap/nselib/smb.lua
install -m 0755 /usr/share/nmap/nselib/smb2.lua	%{buildroot}/usr/share/nmap/nselib/smb2.lua
install -m 0755 /usr/share/nmap/nselib/smbauth.lua	%{buildroot}/usr/share/nmap/nselib/smbauth.lua
install -m 0755 /usr/share/nmap/nselib/smtp.lua	%{buildroot}/usr/share/nmap/nselib/smtp.lua
install -m 0755 /usr/share/nmap/nselib/snmp.lua	%{buildroot}/usr/share/nmap/nselib/snmp.lua
install -m 0755 /usr/share/nmap/nselib/socks.lua	%{buildroot}/usr/share/nmap/nselib/socks.lua
install -m 0755 /usr/share/nmap/nselib/srvloc.lua	%{buildroot}/usr/share/nmap/nselib/srvloc.lua
install -m 0755 /usr/share/nmap/nselib/ssh1.lua	%{buildroot}/usr/share/nmap/nselib/ssh1.lua
install -m 0755 /usr/share/nmap/nselib/ssh2.lua	%{buildroot}/usr/share/nmap/nselib/ssh2.lua
install -m 0755 /usr/share/nmap/nselib/sslcert.lua	%{buildroot}/usr/share/nmap/nselib/sslcert.lua
install -m 0755 /usr/share/nmap/nselib/sslv2.lua	%{buildroot}/usr/share/nmap/nselib/sslv2.lua
install -m 0755 /usr/share/nmap/nselib/stdnse.lua	%{buildroot}/usr/share/nmap/nselib/stdnse.lua
install -m 0755 /usr/share/nmap/nselib/strbuf.lua	%{buildroot}/usr/share/nmap/nselib/strbuf.lua
install -m 0755 /usr/share/nmap/nselib/strict.lua	%{buildroot}/usr/share/nmap/nselib/strict.lua
install -m 0755 /usr/share/nmap/nselib/stringaux.lua	%{buildroot}/usr/share/nmap/nselib/stringaux.lua
install -m 0755 /usr/share/nmap/nselib/stun.lua	%{buildroot}/usr/share/nmap/nselib/stun.lua
install -m 0755 /usr/share/nmap/nselib/tab.lua	%{buildroot}/usr/share/nmap/nselib/tab.lua
install -m 0755 /usr/share/nmap/nselib/tableaux.lua	%{buildroot}/usr/share/nmap/nselib/tableaux.lua
install -m 0755 /usr/share/nmap/nselib/target.lua	%{buildroot}/usr/share/nmap/nselib/target.lua
install -m 0755 /usr/share/nmap/nselib/tftp.lua	%{buildroot}/usr/share/nmap/nselib/tftp.lua
install -m 0755 /usr/share/nmap/nselib/tls.lua	%{buildroot}/usr/share/nmap/nselib/tls.lua
install -m 0755 /usr/share/nmap/nselib/tn3270.lua	%{buildroot}/usr/share/nmap/nselib/tn3270.lua
install -m 0755 /usr/share/nmap/nselib/tns.lua	%{buildroot}/usr/share/nmap/nselib/tns.lua
install -m 0755 /usr/share/nmap/nselib/unicode.lua	%{buildroot}/usr/share/nmap/nselib/unicode.lua
install -m 0755 /usr/share/nmap/nselib/unittest.lua	%{buildroot}/usr/share/nmap/nselib/unittest.lua
install -m 0755 /usr/share/nmap/nselib/unpwdb.lua	%{buildroot}/usr/share/nmap/nselib/unpwdb.lua
install -m 0755 /usr/share/nmap/nselib/upnp.lua	%{buildroot}/usr/share/nmap/nselib/upnp.lua
install -m 0755 /usr/share/nmap/nselib/url.lua	%{buildroot}/usr/share/nmap/nselib/url.lua
install -m 0755 /usr/share/nmap/nselib/versant.lua	%{buildroot}/usr/share/nmap/nselib/versant.lua
install -m 0755 /usr/share/nmap/nselib/vnc.lua	%{buildroot}/usr/share/nmap/nselib/vnc.lua
install -m 0755 /usr/share/nmap/nselib/vulns.lua	%{buildroot}/usr/share/nmap/nselib/vulns.lua
install -m 0755 /usr/share/nmap/nselib/vuzedht.lua	%{buildroot}/usr/share/nmap/nselib/vuzedht.lua
install -m 0755 /usr/share/nmap/nselib/wsdd.lua	%{buildroot}/usr/share/nmap/nselib/wsdd.lua
install -m 0755 /usr/share/nmap/nselib/xdmcp.lua	%{buildroot}/usr/share/nmap/nselib/xdmcp.lua
install -m 0755 /usr/share/nmap/nselib/xmpp.lua	%{buildroot}/usr/share/nmap/nselib/xmpp.lua
install -m 0755 /usr/share/nmap/nselib/zlib.luadoc	%{buildroot}/usr/share/nmap/nselib/zlib.luadoc
install -m 0755 /usr/share/nmap/scripts/acarsd-info.nse	%{buildroot}/usr/share/nmap/scripts/acarsd-info.nse
install -m 0755 /usr/share/nmap/scripts/address-info.nse	%{buildroot}/usr/share/nmap/scripts/address-info.nse
install -m 0755 /usr/share/nmap/scripts/afp-brute.nse	%{buildroot}/usr/share/nmap/scripts/afp-brute.nse
install -m 0755 /usr/share/nmap/scripts/afp-ls.nse	%{buildroot}/usr/share/nmap/scripts/afp-ls.nse
install -m 0755 /usr/share/nmap/scripts/afp-path-vuln.nse	%{buildroot}/usr/share/nmap/scripts/afp-path-vuln.nse
install -m 0755 /usr/share/nmap/scripts/afp-serverinfo.nse	%{buildroot}/usr/share/nmap/scripts/afp-serverinfo.nse
install -m 0755 /usr/share/nmap/scripts/afp-showmount.nse	%{buildroot}/usr/share/nmap/scripts/afp-showmount.nse
install -m 0755 /usr/share/nmap/scripts/ajp-auth.nse	%{buildroot}/usr/share/nmap/scripts/ajp-auth.nse
install -m 0755 /usr/share/nmap/scripts/ajp-brute.nse	%{buildroot}/usr/share/nmap/scripts/ajp-brute.nse
install -m 0755 /usr/share/nmap/scripts/ajp-headers.nse	%{buildroot}/usr/share/nmap/scripts/ajp-headers.nse
install -m 0755 /usr/share/nmap/scripts/ajp-methods.nse	%{buildroot}/usr/share/nmap/scripts/ajp-methods.nse
install -m 0755 /usr/share/nmap/scripts/ajp-request.nse	%{buildroot}/usr/share/nmap/scripts/ajp-request.nse
install -m 0755 /usr/share/nmap/scripts/allseeingeye-info.nse	%{buildroot}/usr/share/nmap/scripts/allseeingeye-info.nse
install -m 0755 /usr/share/nmap/scripts/amqp-info.nse	%{buildroot}/usr/share/nmap/scripts/amqp-info.nse
install -m 0755 /usr/share/nmap/scripts/asn-query.nse	%{buildroot}/usr/share/nmap/scripts/asn-query.nse
install -m 0755 /usr/share/nmap/scripts/auth-owners.nse	%{buildroot}/usr/share/nmap/scripts/auth-owners.nse
install -m 0755 /usr/share/nmap/scripts/auth-spoof.nse	%{buildroot}/usr/share/nmap/scripts/auth-spoof.nse
install -m 0755 /usr/share/nmap/scripts/backorifice-brute.nse	%{buildroot}/usr/share/nmap/scripts/backorifice-brute.nse
install -m 0755 /usr/share/nmap/scripts/backorifice-info.nse	%{buildroot}/usr/share/nmap/scripts/backorifice-info.nse
install -m 0755 /usr/share/nmap/scripts/bacnet-info.nse	%{buildroot}/usr/share/nmap/scripts/bacnet-info.nse
install -m 0755 /usr/share/nmap/scripts/banner.nse	%{buildroot}/usr/share/nmap/scripts/banner.nse
install -m 0755 /usr/share/nmap/scripts/bitcoin-getaddr.nse	%{buildroot}/usr/share/nmap/scripts/bitcoin-getaddr.nse
install -m 0755 /usr/share/nmap/scripts/bitcoin-info.nse	%{buildroot}/usr/share/nmap/scripts/bitcoin-info.nse
install -m 0755 /usr/share/nmap/scripts/bitcoinrpc-info.nse	%{buildroot}/usr/share/nmap/scripts/bitcoinrpc-info.nse
install -m 0755 /usr/share/nmap/scripts/bittorrent-discovery.nse	%{buildroot}/usr/share/nmap/scripts/bittorrent-discovery.nse
install -m 0755 /usr/share/nmap/scripts/bjnp-discover.nse	%{buildroot}/usr/share/nmap/scripts/bjnp-discover.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-ataoe-discover.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-ataoe-discover.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-avahi-dos.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-avahi-dos.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-bjnp-discover.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-bjnp-discover.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-db2-discover.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-db2-discover.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-dhcp-discover.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-dhcp-discover.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-dhcp6-discover.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-dhcp6-discover.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-dns-service-discovery.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-dns-service-discovery.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-dropbox-listener.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-dropbox-listener.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-eigrp-discovery.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-eigrp-discovery.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-hid-discoveryd.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-hid-discoveryd.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-igmp-discovery.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-igmp-discovery.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-jenkins-discover.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-jenkins-discover.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-listener.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-listener.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-ms-sql-discover.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-ms-sql-discover.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-netbios-master-browser.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-netbios-master-browser.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-networker-discover.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-networker-discover.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-novell-locate.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-novell-locate.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-ospf2-discover.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-ospf2-discover.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-pc-anywhere.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-pc-anywhere.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-pc-duo.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-pc-duo.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-pim-discovery.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-pim-discovery.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-ping.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-ping.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-pppoe-discover.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-pppoe-discover.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-rip-discover.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-rip-discover.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-ripng-discover.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-ripng-discover.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-sonicwall-discover.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-sonicwall-discover.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-sybase-asa-discover.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-sybase-asa-discover.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-tellstick-discover.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-tellstick-discover.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-upnp-info.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-upnp-info.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-versant-locate.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-versant-locate.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-wake-on-lan.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-wake-on-lan.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-wpad-discover.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-wpad-discover.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-wsdd-discover.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-wsdd-discover.nse
install -m 0755 /usr/share/nmap/scripts/broadcast-xdmcp-discover.nse	%{buildroot}/usr/share/nmap/scripts/broadcast-xdmcp-discover.nse
install -m 0755 /usr/share/nmap/scripts/cassandra-brute.nse	%{buildroot}/usr/share/nmap/scripts/cassandra-brute.nse
install -m 0755 /usr/share/nmap/scripts/cassandra-info.nse	%{buildroot}/usr/share/nmap/scripts/cassandra-info.nse
install -m 0755 /usr/share/nmap/scripts/cccam-version.nse	%{buildroot}/usr/share/nmap/scripts/cccam-version.nse
install -m 0755 /usr/share/nmap/scripts/cics-enum.nse	%{buildroot}/usr/share/nmap/scripts/cics-enum.nse
install -m 0755 /usr/share/nmap/scripts/cics-info.nse	%{buildroot}/usr/share/nmap/scripts/cics-info.nse
install -m 0755 /usr/share/nmap/scripts/cics-user-brute.nse	%{buildroot}/usr/share/nmap/scripts/cics-user-brute.nse
install -m 0755 /usr/share/nmap/scripts/cics-user-enum.nse	%{buildroot}/usr/share/nmap/scripts/cics-user-enum.nse
install -m 0755 /usr/share/nmap/scripts/citrix-brute-xml.nse	%{buildroot}/usr/share/nmap/scripts/citrix-brute-xml.nse
install -m 0755 /usr/share/nmap/scripts/citrix-enum-apps-xml.nse	%{buildroot}/usr/share/nmap/scripts/citrix-enum-apps-xml.nse
install -m 0755 /usr/share/nmap/scripts/citrix-enum-apps.nse	%{buildroot}/usr/share/nmap/scripts/citrix-enum-apps.nse
install -m 0755 /usr/share/nmap/scripts/citrix-enum-servers-xml.nse	%{buildroot}/usr/share/nmap/scripts/citrix-enum-servers-xml.nse
install -m 0755 /usr/share/nmap/scripts/citrix-enum-servers.nse	%{buildroot}/usr/share/nmap/scripts/citrix-enum-servers.nse
install -m 0755 /usr/share/nmap/scripts/clamav-exec.nse	%{buildroot}/usr/share/nmap/scripts/clamav-exec.nse
install -m 0755 /usr/share/nmap/scripts/clock-skew.nse	%{buildroot}/usr/share/nmap/scripts/clock-skew.nse
install -m 0755 /usr/share/nmap/scripts/coap-resources.nse	%{buildroot}/usr/share/nmap/scripts/coap-resources.nse
install -m 0755 /usr/share/nmap/scripts/couchdb-databases.nse	%{buildroot}/usr/share/nmap/scripts/couchdb-databases.nse
install -m 0755 /usr/share/nmap/scripts/couchdb-stats.nse	%{buildroot}/usr/share/nmap/scripts/couchdb-stats.nse
install -m 0755 /usr/share/nmap/scripts/creds-summary.nse	%{buildroot}/usr/share/nmap/scripts/creds-summary.nse
install -m 0755 /usr/share/nmap/scripts/cups-info.nse	%{buildroot}/usr/share/nmap/scripts/cups-info.nse
install -m 0755 /usr/share/nmap/scripts/cups-queue-info.nse	%{buildroot}/usr/share/nmap/scripts/cups-queue-info.nse
install -m 0755 /usr/share/nmap/scripts/cvs-brute-repository.nse	%{buildroot}/usr/share/nmap/scripts/cvs-brute-repository.nse
install -m 0755 /usr/share/nmap/scripts/cvs-brute.nse	%{buildroot}/usr/share/nmap/scripts/cvs-brute.nse
install -m 0755 /usr/share/nmap/scripts/daap-get-library.nse	%{buildroot}/usr/share/nmap/scripts/daap-get-library.nse
install -m 0755 /usr/share/nmap/scripts/daytime.nse	%{buildroot}/usr/share/nmap/scripts/daytime.nse
install -m 0755 /usr/share/nmap/scripts/db2-das-info.nse	%{buildroot}/usr/share/nmap/scripts/db2-das-info.nse
install -m 0755 /usr/share/nmap/scripts/deluge-rpc-brute.nse	%{buildroot}/usr/share/nmap/scripts/deluge-rpc-brute.nse
install -m 0755 /usr/share/nmap/scripts/dhcp-discover.nse	%{buildroot}/usr/share/nmap/scripts/dhcp-discover.nse
install -m 0755 /usr/share/nmap/scripts/dict-info.nse	%{buildroot}/usr/share/nmap/scripts/dict-info.nse
install -m 0755 /usr/share/nmap/scripts/distcc-cve2004-2687.nse	%{buildroot}/usr/share/nmap/scripts/distcc-cve2004-2687.nse
install -m 0755 /usr/share/nmap/scripts/dns-blacklist.nse	%{buildroot}/usr/share/nmap/scripts/dns-blacklist.nse
install -m 0755 /usr/share/nmap/scripts/dns-brute.nse	%{buildroot}/usr/share/nmap/scripts/dns-brute.nse
install -m 0755 /usr/share/nmap/scripts/dns-cache-snoop.nse	%{buildroot}/usr/share/nmap/scripts/dns-cache-snoop.nse
install -m 0755 /usr/share/nmap/scripts/dns-check-zone.nse	%{buildroot}/usr/share/nmap/scripts/dns-check-zone.nse
install -m 0755 /usr/share/nmap/scripts/dns-client-subnet-scan.nse	%{buildroot}/usr/share/nmap/scripts/dns-client-subnet-scan.nse
install -m 0755 /usr/share/nmap/scripts/dns-fuzz.nse	%{buildroot}/usr/share/nmap/scripts/dns-fuzz.nse
install -m 0755 /usr/share/nmap/scripts/dns-ip6-arpa-scan.nse	%{buildroot}/usr/share/nmap/scripts/dns-ip6-arpa-scan.nse
install -m 0755 /usr/share/nmap/scripts/dns-nsec-enum.nse	%{buildroot}/usr/share/nmap/scripts/dns-nsec-enum.nse
install -m 0755 /usr/share/nmap/scripts/dns-nsec3-enum.nse	%{buildroot}/usr/share/nmap/scripts/dns-nsec3-enum.nse
install -m 0755 /usr/share/nmap/scripts/dns-nsid.nse	%{buildroot}/usr/share/nmap/scripts/dns-nsid.nse
install -m 0755 /usr/share/nmap/scripts/dns-random-srcport.nse	%{buildroot}/usr/share/nmap/scripts/dns-random-srcport.nse
install -m 0755 /usr/share/nmap/scripts/dns-random-txid.nse	%{buildroot}/usr/share/nmap/scripts/dns-random-txid.nse
install -m 0755 /usr/share/nmap/scripts/dns-recursion.nse	%{buildroot}/usr/share/nmap/scripts/dns-recursion.nse
install -m 0755 /usr/share/nmap/scripts/dns-service-discovery.nse	%{buildroot}/usr/share/nmap/scripts/dns-service-discovery.nse
install -m 0755 /usr/share/nmap/scripts/dns-srv-enum.nse	%{buildroot}/usr/share/nmap/scripts/dns-srv-enum.nse
install -m 0755 /usr/share/nmap/scripts/dns-update.nse	%{buildroot}/usr/share/nmap/scripts/dns-update.nse
install -m 0755 /usr/share/nmap/scripts/dns-zeustracker.nse	%{buildroot}/usr/share/nmap/scripts/dns-zeustracker.nse
install -m 0755 /usr/share/nmap/scripts/dns-zone-transfer.nse	%{buildroot}/usr/share/nmap/scripts/dns-zone-transfer.nse
install -m 0755 /usr/share/nmap/scripts/docker-version.nse	%{buildroot}/usr/share/nmap/scripts/docker-version.nse
install -m 0755 /usr/share/nmap/scripts/domcon-brute.nse	%{buildroot}/usr/share/nmap/scripts/domcon-brute.nse
install -m 0755 /usr/share/nmap/scripts/domcon-cmd.nse	%{buildroot}/usr/share/nmap/scripts/domcon-cmd.nse
install -m 0755 /usr/share/nmap/scripts/domino-enum-users.nse	%{buildroot}/usr/share/nmap/scripts/domino-enum-users.nse
install -m 0755 /usr/share/nmap/scripts/dpap-brute.nse	%{buildroot}/usr/share/nmap/scripts/dpap-brute.nse
install -m 0755 /usr/share/nmap/scripts/drda-brute.nse	%{buildroot}/usr/share/nmap/scripts/drda-brute.nse
install -m 0755 /usr/share/nmap/scripts/drda-info.nse	%{buildroot}/usr/share/nmap/scripts/drda-info.nse
install -m 0755 /usr/share/nmap/scripts/duplicates.nse	%{buildroot}/usr/share/nmap/scripts/duplicates.nse
install -m 0755 /usr/share/nmap/scripts/eap-info.nse	%{buildroot}/usr/share/nmap/scripts/eap-info.nse
install -m 0755 /usr/share/nmap/scripts/enip-info.nse	%{buildroot}/usr/share/nmap/scripts/enip-info.nse
install -m 0755 /usr/share/nmap/scripts/epmd-info.nse	%{buildroot}/usr/share/nmap/scripts/epmd-info.nse
install -m 0755 /usr/share/nmap/scripts/eppc-enum-processes.nse	%{buildroot}/usr/share/nmap/scripts/eppc-enum-processes.nse
install -m 0755 /usr/share/nmap/scripts/fcrdns.nse	%{buildroot}/usr/share/nmap/scripts/fcrdns.nse
install -m 0755 /usr/share/nmap/scripts/finger.nse	%{buildroot}/usr/share/nmap/scripts/finger.nse
install -m 0755 /usr/share/nmap/scripts/fingerprint-strings.nse	%{buildroot}/usr/share/nmap/scripts/fingerprint-strings.nse
install -m 0755 /usr/share/nmap/scripts/firewalk.nse	%{buildroot}/usr/share/nmap/scripts/firewalk.nse
install -m 0755 /usr/share/nmap/scripts/firewall-bypass.nse	%{buildroot}/usr/share/nmap/scripts/firewall-bypass.nse
install -m 0755 /usr/share/nmap/scripts/flume-master-info.nse	%{buildroot}/usr/share/nmap/scripts/flume-master-info.nse
install -m 0755 /usr/share/nmap/scripts/fox-info.nse	%{buildroot}/usr/share/nmap/scripts/fox-info.nse
install -m 0755 /usr/share/nmap/scripts/freelancer-info.nse	%{buildroot}/usr/share/nmap/scripts/freelancer-info.nse
install -m 0755 /usr/share/nmap/scripts/ftp-anon.nse	%{buildroot}/usr/share/nmap/scripts/ftp-anon.nse
install -m 0755 /usr/share/nmap/scripts/ftp-bounce.nse	%{buildroot}/usr/share/nmap/scripts/ftp-bounce.nse
install -m 0755 /usr/share/nmap/scripts/ftp-brute.nse	%{buildroot}/usr/share/nmap/scripts/ftp-brute.nse
install -m 0755 /usr/share/nmap/scripts/ftp-libopie.nse	%{buildroot}/usr/share/nmap/scripts/ftp-libopie.nse
install -m 0755 /usr/share/nmap/scripts/ftp-proftpd-backdoor.nse	%{buildroot}/usr/share/nmap/scripts/ftp-proftpd-backdoor.nse
install -m 0755 /usr/share/nmap/scripts/ftp-syst.nse	%{buildroot}/usr/share/nmap/scripts/ftp-syst.nse
install -m 0755 /usr/share/nmap/scripts/ftp-vsftpd-backdoor.nse	%{buildroot}/usr/share/nmap/scripts/ftp-vsftpd-backdoor.nse
install -m 0755 /usr/share/nmap/scripts/ftp-vuln-cve2010-4221.nse	%{buildroot}/usr/share/nmap/scripts/ftp-vuln-cve2010-4221.nse
install -m 0755 /usr/share/nmap/scripts/ganglia-info.nse	%{buildroot}/usr/share/nmap/scripts/ganglia-info.nse
install -m 0755 /usr/share/nmap/scripts/giop-info.nse	%{buildroot}/usr/share/nmap/scripts/giop-info.nse
install -m 0755 /usr/share/nmap/scripts/gkrellm-info.nse	%{buildroot}/usr/share/nmap/scripts/gkrellm-info.nse
install -m 0755 /usr/share/nmap/scripts/gopher-ls.nse	%{buildroot}/usr/share/nmap/scripts/gopher-ls.nse
install -m 0755 /usr/share/nmap/scripts/gpsd-info.nse	%{buildroot}/usr/share/nmap/scripts/gpsd-info.nse
install -m 0755 /usr/share/nmap/scripts/hadoop-datanode-info.nse	%{buildroot}/usr/share/nmap/scripts/hadoop-datanode-info.nse
install -m 0755 /usr/share/nmap/scripts/hadoop-jobtracker-info.nse	%{buildroot}/usr/share/nmap/scripts/hadoop-jobtracker-info.nse
install -m 0755 /usr/share/nmap/scripts/hadoop-namenode-info.nse	%{buildroot}/usr/share/nmap/scripts/hadoop-namenode-info.nse
install -m 0755 /usr/share/nmap/scripts/hadoop-secondary-namenode-info.nse	%{buildroot}/usr/share/nmap/scripts/hadoop-secondary-namenode-info.nse
install -m 0755 /usr/share/nmap/scripts/hadoop-tasktracker-info.nse	%{buildroot}/usr/share/nmap/scripts/hadoop-tasktracker-info.nse
install -m 0755 /usr/share/nmap/scripts/hbase-master-info.nse	%{buildroot}/usr/share/nmap/scripts/hbase-master-info.nse
install -m 0755 /usr/share/nmap/scripts/hbase-region-info.nse	%{buildroot}/usr/share/nmap/scripts/hbase-region-info.nse
install -m 0755 /usr/share/nmap/scripts/hddtemp-info.nse	%{buildroot}/usr/share/nmap/scripts/hddtemp-info.nse
install -m 0755 /usr/share/nmap/scripts/hnap-info.nse	%{buildroot}/usr/share/nmap/scripts/hnap-info.nse
install -m 0755 /usr/share/nmap/scripts/hostmap-bfk.nse	%{buildroot}/usr/share/nmap/scripts/hostmap-bfk.nse
install -m 0755 /usr/share/nmap/scripts/hostmap-crtsh.nse	%{buildroot}/usr/share/nmap/scripts/hostmap-crtsh.nse
install -m 0755 /usr/share/nmap/scripts/hostmap-robtex.nse	%{buildroot}/usr/share/nmap/scripts/hostmap-robtex.nse
install -m 0755 /usr/share/nmap/scripts/http-adobe-coldfusion-apsa1301.nse	%{buildroot}/usr/share/nmap/scripts/http-adobe-coldfusion-apsa1301.nse
install -m 0755 /usr/share/nmap/scripts/http-affiliate-id.nse	%{buildroot}/usr/share/nmap/scripts/http-affiliate-id.nse
install -m 0755 /usr/share/nmap/scripts/http-apache-negotiation.nse	%{buildroot}/usr/share/nmap/scripts/http-apache-negotiation.nse
install -m 0755 /usr/share/nmap/scripts/http-apache-server-status.nse	%{buildroot}/usr/share/nmap/scripts/http-apache-server-status.nse
install -m 0755 /usr/share/nmap/scripts/http-aspnet-debug.nse	%{buildroot}/usr/share/nmap/scripts/http-aspnet-debug.nse
install -m 0755 /usr/share/nmap/scripts/http-auth-finder.nse	%{buildroot}/usr/share/nmap/scripts/http-auth-finder.nse
install -m 0755 /usr/share/nmap/scripts/http-auth.nse	%{buildroot}/usr/share/nmap/scripts/http-auth.nse
install -m 0755 /usr/share/nmap/scripts/http-avaya-ipoffice-users.nse	%{buildroot}/usr/share/nmap/scripts/http-avaya-ipoffice-users.nse
install -m 0755 /usr/share/nmap/scripts/http-awstatstotals-exec.nse	%{buildroot}/usr/share/nmap/scripts/http-awstatstotals-exec.nse
install -m 0755 /usr/share/nmap/scripts/http-axis2-dir-traversal.nse	%{buildroot}/usr/share/nmap/scripts/http-axis2-dir-traversal.nse
install -m 0755 /usr/share/nmap/scripts/http-backup-finder.nse	%{buildroot}/usr/share/nmap/scripts/http-backup-finder.nse
install -m 0755 /usr/share/nmap/scripts/http-barracuda-dir-traversal.nse	%{buildroot}/usr/share/nmap/scripts/http-barracuda-dir-traversal.nse
install -m 0755 /usr/share/nmap/scripts/http-bigip-cookie.nse	%{buildroot}/usr/share/nmap/scripts/http-bigip-cookie.nse
install -m 0755 /usr/share/nmap/scripts/http-brute.nse	%{buildroot}/usr/share/nmap/scripts/http-brute.nse
install -m 0755 /usr/share/nmap/scripts/http-cakephp-version.nse	%{buildroot}/usr/share/nmap/scripts/http-cakephp-version.nse
install -m 0755 /usr/share/nmap/scripts/http-chrono.nse	%{buildroot}/usr/share/nmap/scripts/http-chrono.nse
install -m 0755 /usr/share/nmap/scripts/http-cisco-anyconnect.nse	%{buildroot}/usr/share/nmap/scripts/http-cisco-anyconnect.nse
install -m 0755 /usr/share/nmap/scripts/http-coldfusion-subzero.nse	%{buildroot}/usr/share/nmap/scripts/http-coldfusion-subzero.nse
install -m 0755 /usr/share/nmap/scripts/http-comments-displayer.nse	%{buildroot}/usr/share/nmap/scripts/http-comments-displayer.nse
install -m 0755 /usr/share/nmap/scripts/http-config-backup.nse	%{buildroot}/usr/share/nmap/scripts/http-config-backup.nse
install -m 0755 /usr/share/nmap/scripts/http-cookie-flags.nse	%{buildroot}/usr/share/nmap/scripts/http-cookie-flags.nse
install -m 0755 /usr/share/nmap/scripts/http-cors.nse	%{buildroot}/usr/share/nmap/scripts/http-cors.nse
install -m 0755 /usr/share/nmap/scripts/http-cross-domain-policy.nse	%{buildroot}/usr/share/nmap/scripts/http-cross-domain-policy.nse
install -m 0755 /usr/share/nmap/scripts/http-csrf.nse	%{buildroot}/usr/share/nmap/scripts/http-csrf.nse
install -m 0755 /usr/share/nmap/scripts/http-date.nse	%{buildroot}/usr/share/nmap/scripts/http-date.nse
install -m 0755 /usr/share/nmap/scripts/http-default-accounts.nse	%{buildroot}/usr/share/nmap/scripts/http-default-accounts.nse
install -m 0755 /usr/share/nmap/scripts/http-devframework.nse	%{buildroot}/usr/share/nmap/scripts/http-devframework.nse
install -m 0755 /usr/share/nmap/scripts/http-dlink-backdoor.nse	%{buildroot}/usr/share/nmap/scripts/http-dlink-backdoor.nse
install -m 0755 /usr/share/nmap/scripts/http-dombased-xss.nse	%{buildroot}/usr/share/nmap/scripts/http-dombased-xss.nse
install -m 0755 /usr/share/nmap/scripts/http-domino-enum-passwords.nse	%{buildroot}/usr/share/nmap/scripts/http-domino-enum-passwords.nse
install -m 0755 /usr/share/nmap/scripts/http-drupal-enum-users.nse	%{buildroot}/usr/share/nmap/scripts/http-drupal-enum-users.nse
install -m 0755 /usr/share/nmap/scripts/http-drupal-enum.nse	%{buildroot}/usr/share/nmap/scripts/http-drupal-enum.nse
install -m 0755 /usr/share/nmap/scripts/http-enum.nse	%{buildroot}/usr/share/nmap/scripts/http-enum.nse
install -m 0755 /usr/share/nmap/scripts/http-errors.nse	%{buildroot}/usr/share/nmap/scripts/http-errors.nse
install -m 0755 /usr/share/nmap/scripts/http-exif-spider.nse	%{buildroot}/usr/share/nmap/scripts/http-exif-spider.nse
install -m 0755 /usr/share/nmap/scripts/http-favicon.nse	%{buildroot}/usr/share/nmap/scripts/http-favicon.nse
install -m 0755 /usr/share/nmap/scripts/http-feed.nse	%{buildroot}/usr/share/nmap/scripts/http-feed.nse
install -m 0755 /usr/share/nmap/scripts/http-fetch.nse	%{buildroot}/usr/share/nmap/scripts/http-fetch.nse
install -m 0755 /usr/share/nmap/scripts/http-fileupload-exploiter.nse	%{buildroot}/usr/share/nmap/scripts/http-fileupload-exploiter.nse
install -m 0755 /usr/share/nmap/scripts/http-form-brute.nse	%{buildroot}/usr/share/nmap/scripts/http-form-brute.nse
install -m 0755 /usr/share/nmap/scripts/http-form-fuzzer.nse	%{buildroot}/usr/share/nmap/scripts/http-form-fuzzer.nse
install -m 0755 /usr/share/nmap/scripts/http-frontpage-login.nse	%{buildroot}/usr/share/nmap/scripts/http-frontpage-login.nse
install -m 0755 /usr/share/nmap/scripts/http-generator.nse	%{buildroot}/usr/share/nmap/scripts/http-generator.nse
install -m 0755 /usr/share/nmap/scripts/http-git.nse	%{buildroot}/usr/share/nmap/scripts/http-git.nse
install -m 0755 /usr/share/nmap/scripts/http-gitweb-projects-enum.nse	%{buildroot}/usr/share/nmap/scripts/http-gitweb-projects-enum.nse
install -m 0755 /usr/share/nmap/scripts/http-google-malware.nse	%{buildroot}/usr/share/nmap/scripts/http-google-malware.nse
install -m 0755 /usr/share/nmap/scripts/http-grep.nse	%{buildroot}/usr/share/nmap/scripts/http-grep.nse
install -m 0755 /usr/share/nmap/scripts/http-headers.nse	%{buildroot}/usr/share/nmap/scripts/http-headers.nse
install -m 0755 /usr/share/nmap/scripts/http-hp-ilo-info.nse	%{buildroot}/usr/share/nmap/scripts/http-hp-ilo-info.nse
install -m 0755 /usr/share/nmap/scripts/http-huawei-hg5xx-vuln.nse	%{buildroot}/usr/share/nmap/scripts/http-huawei-hg5xx-vuln.nse
install -m 0755 /usr/share/nmap/scripts/http-icloud-findmyiphone.nse	%{buildroot}/usr/share/nmap/scripts/http-icloud-findmyiphone.nse
install -m 0755 /usr/share/nmap/scripts/http-icloud-sendmsg.nse	%{buildroot}/usr/share/nmap/scripts/http-icloud-sendmsg.nse
install -m 0755 /usr/share/nmap/scripts/http-iis-short-name-brute.nse	%{buildroot}/usr/share/nmap/scripts/http-iis-short-name-brute.nse
install -m 0755 /usr/share/nmap/scripts/http-iis-webdav-vuln.nse	%{buildroot}/usr/share/nmap/scripts/http-iis-webdav-vuln.nse
install -m 0755 /usr/share/nmap/scripts/http-internal-ip-disclosure.nse	%{buildroot}/usr/share/nmap/scripts/http-internal-ip-disclosure.nse
install -m 0755 /usr/share/nmap/scripts/http-joomla-brute.nse	%{buildroot}/usr/share/nmap/scripts/http-joomla-brute.nse
install -m 0755 /usr/share/nmap/scripts/http-jsonp-detection.nse	%{buildroot}/usr/share/nmap/scripts/http-jsonp-detection.nse
install -m 0755 /usr/share/nmap/scripts/http-litespeed-sourcecode-download.nse	%{buildroot}/usr/share/nmap/scripts/http-litespeed-sourcecode-download.nse
install -m 0755 /usr/share/nmap/scripts/http-ls.nse	%{buildroot}/usr/share/nmap/scripts/http-ls.nse
install -m 0755 /usr/share/nmap/scripts/http-majordomo2-dir-traversal.nse	%{buildroot}/usr/share/nmap/scripts/http-majordomo2-dir-traversal.nse
install -m 0755 /usr/share/nmap/scripts/http-malware-host.nse	%{buildroot}/usr/share/nmap/scripts/http-malware-host.nse
install -m 0755 /usr/share/nmap/scripts/http-mcmp.nse	%{buildroot}/usr/share/nmap/scripts/http-mcmp.nse
install -m 0755 /usr/share/nmap/scripts/http-method-tamper.nse	%{buildroot}/usr/share/nmap/scripts/http-method-tamper.nse
install -m 0755 /usr/share/nmap/scripts/http-methods.nse	%{buildroot}/usr/share/nmap/scripts/http-methods.nse
install -m 0755 /usr/share/nmap/scripts/http-mobileversion-checker.nse	%{buildroot}/usr/share/nmap/scripts/http-mobileversion-checker.nse
install -m 0755 /usr/share/nmap/scripts/http-ntlm-info.nse	%{buildroot}/usr/share/nmap/scripts/http-ntlm-info.nse
install -m 0755 /usr/share/nmap/scripts/http-open-proxy.nse	%{buildroot}/usr/share/nmap/scripts/http-open-proxy.nse
install -m 0755 /usr/share/nmap/scripts/http-open-redirect.nse	%{buildroot}/usr/share/nmap/scripts/http-open-redirect.nse
install -m 0755 /usr/share/nmap/scripts/http-passwd.nse	%{buildroot}/usr/share/nmap/scripts/http-passwd.nse
install -m 0755 /usr/share/nmap/scripts/http-php-version.nse	%{buildroot}/usr/share/nmap/scripts/http-php-version.nse
install -m 0755 /usr/share/nmap/scripts/http-phpmyadmin-dir-traversal.nse	%{buildroot}/usr/share/nmap/scripts/http-phpmyadmin-dir-traversal.nse
install -m 0755 /usr/share/nmap/scripts/http-phpself-xss.nse	%{buildroot}/usr/share/nmap/scripts/http-phpself-xss.nse
install -m 0755 /usr/share/nmap/scripts/http-proxy-brute.nse	%{buildroot}/usr/share/nmap/scripts/http-proxy-brute.nse
install -m 0755 /usr/share/nmap/scripts/http-put.nse	%{buildroot}/usr/share/nmap/scripts/http-put.nse
install -m 0755 /usr/share/nmap/scripts/http-qnap-nas-info.nse	%{buildroot}/usr/share/nmap/scripts/http-qnap-nas-info.nse
install -m 0755 /usr/share/nmap/scripts/http-referer-checker.nse	%{buildroot}/usr/share/nmap/scripts/http-referer-checker.nse
install -m 0755 /usr/share/nmap/scripts/http-rfi-spider.nse	%{buildroot}/usr/share/nmap/scripts/http-rfi-spider.nse
install -m 0755 /usr/share/nmap/scripts/http-robots.txt.nse	%{buildroot}/usr/share/nmap/scripts/http-robots.txt.nse
install -m 0755 /usr/share/nmap/scripts/http-robtex-reverse-ip.nse	%{buildroot}/usr/share/nmap/scripts/http-robtex-reverse-ip.nse
install -m 0755 /usr/share/nmap/scripts/http-robtex-shared-ns.nse	%{buildroot}/usr/share/nmap/scripts/http-robtex-shared-ns.nse
install -m 0755 /usr/share/nmap/scripts/http-sap-netweaver-leak.nse	%{buildroot}/usr/share/nmap/scripts/http-sap-netweaver-leak.nse
install -m 0755 /usr/share/nmap/scripts/http-security-headers.nse	%{buildroot}/usr/share/nmap/scripts/http-security-headers.nse
install -m 0755 /usr/share/nmap/scripts/http-server-header.nse	%{buildroot}/usr/share/nmap/scripts/http-server-header.nse
install -m 0755 /usr/share/nmap/scripts/http-shellshock.nse	%{buildroot}/usr/share/nmap/scripts/http-shellshock.nse
install -m 0755 /usr/share/nmap/scripts/http-sitemap-generator.nse	%{buildroot}/usr/share/nmap/scripts/http-sitemap-generator.nse
install -m 0755 /usr/share/nmap/scripts/http-slowloris-check.nse	%{buildroot}/usr/share/nmap/scripts/http-slowloris-check.nse
install -m 0755 /usr/share/nmap/scripts/http-slowloris.nse	%{buildroot}/usr/share/nmap/scripts/http-slowloris.nse
install -m 0755 /usr/share/nmap/scripts/http-sql-injection.nse	%{buildroot}/usr/share/nmap/scripts/http-sql-injection.nse
install -m 0755 /usr/share/nmap/scripts/http-stored-xss.nse	%{buildroot}/usr/share/nmap/scripts/http-stored-xss.nse
install -m 0755 /usr/share/nmap/scripts/http-svn-enum.nse	%{buildroot}/usr/share/nmap/scripts/http-svn-enum.nse
install -m 0755 /usr/share/nmap/scripts/http-svn-info.nse	%{buildroot}/usr/share/nmap/scripts/http-svn-info.nse
install -m 0755 /usr/share/nmap/scripts/http-title.nse	%{buildroot}/usr/share/nmap/scripts/http-title.nse
install -m 0755 /usr/share/nmap/scripts/http-tplink-dir-traversal.nse	%{buildroot}/usr/share/nmap/scripts/http-tplink-dir-traversal.nse
install -m 0755 /usr/share/nmap/scripts/http-trace.nse	%{buildroot}/usr/share/nmap/scripts/http-trace.nse
install -m 0755 /usr/share/nmap/scripts/http-traceroute.nse	%{buildroot}/usr/share/nmap/scripts/http-traceroute.nse
install -m 0755 /usr/share/nmap/scripts/http-trane-info.nse	%{buildroot}/usr/share/nmap/scripts/http-trane-info.nse
install -m 0755 /usr/share/nmap/scripts/http-unsafe-output-escaping.nse	%{buildroot}/usr/share/nmap/scripts/http-unsafe-output-escaping.nse
install -m 0755 /usr/share/nmap/scripts/http-useragent-tester.nse	%{buildroot}/usr/share/nmap/scripts/http-useragent-tester.nse
install -m 0755 /usr/share/nmap/scripts/http-userdir-enum.nse	%{buildroot}/usr/share/nmap/scripts/http-userdir-enum.nse
install -m 0755 /usr/share/nmap/scripts/http-vhosts.nse	%{buildroot}/usr/share/nmap/scripts/http-vhosts.nse
install -m 0755 /usr/share/nmap/scripts/http-virustotal.nse	%{buildroot}/usr/share/nmap/scripts/http-virustotal.nse
install -m 0755 /usr/share/nmap/scripts/http-vlcstreamer-ls.nse	%{buildroot}/usr/share/nmap/scripts/http-vlcstreamer-ls.nse
install -m 0755 /usr/share/nmap/scripts/http-vmware-path-vuln.nse	%{buildroot}/usr/share/nmap/scripts/http-vmware-path-vuln.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2006-3392.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2006-3392.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2009-3960.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2009-3960.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2010-0738.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2010-0738.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2010-2861.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2010-2861.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2011-3192.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2011-3192.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2011-3368.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2011-3368.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2012-1823.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2012-1823.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2013-0156.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2013-0156.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2013-6786.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2013-6786.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2013-7091.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2013-7091.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2014-2126.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2014-2126.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2014-2127.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2014-2127.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2014-2128.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2014-2128.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2014-2129.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2014-2129.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2014-3704.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2014-3704.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2014-8877.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2014-8877.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2015-1427.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2015-1427.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2015-1635.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2015-1635.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2017-1001000.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2017-1001000.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2017-5638.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2017-5638.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2017-5689.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2017-5689.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-cve2017-8917.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-cve2017-8917.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-misfortune-cookie.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-misfortune-cookie.nse
install -m 0755 /usr/share/nmap/scripts/http-vuln-wnr1000-creds.nse	%{buildroot}/usr/share/nmap/scripts/http-vuln-wnr1000-creds.nse
install -m 0755 /usr/share/nmap/scripts/http-waf-detect.nse	%{buildroot}/usr/share/nmap/scripts/http-waf-detect.nse
install -m 0755 /usr/share/nmap/scripts/http-waf-fingerprint.nse	%{buildroot}/usr/share/nmap/scripts/http-waf-fingerprint.nse
install -m 0755 /usr/share/nmap/scripts/http-webdav-scan.nse	%{buildroot}/usr/share/nmap/scripts/http-webdav-scan.nse
install -m 0755 /usr/share/nmap/scripts/http-wordpress-brute.nse	%{buildroot}/usr/share/nmap/scripts/http-wordpress-brute.nse
install -m 0755 /usr/share/nmap/scripts/http-wordpress-enum.nse	%{buildroot}/usr/share/nmap/scripts/http-wordpress-enum.nse
install -m 0755 /usr/share/nmap/scripts/http-wordpress-users.nse	%{buildroot}/usr/share/nmap/scripts/http-wordpress-users.nse
install -m 0755 /usr/share/nmap/scripts/http-xssed.nse	%{buildroot}/usr/share/nmap/scripts/http-xssed.nse
install -m 0755 /usr/share/nmap/scripts/https-redirect.nse	%{buildroot}/usr/share/nmap/scripts/https-redirect.nse
install -m 0755 /usr/share/nmap/scripts/iax2-brute.nse	%{buildroot}/usr/share/nmap/scripts/iax2-brute.nse
install -m 0755 /usr/share/nmap/scripts/iax2-version.nse	%{buildroot}/usr/share/nmap/scripts/iax2-version.nse
install -m 0755 /usr/share/nmap/scripts/icap-info.nse	%{buildroot}/usr/share/nmap/scripts/icap-info.nse
install -m 0755 /usr/share/nmap/scripts/iec-identify.nse	%{buildroot}/usr/share/nmap/scripts/iec-identify.nse
install -m 0755 /usr/share/nmap/scripts/ike-version.nse	%{buildroot}/usr/share/nmap/scripts/ike-version.nse
install -m 0755 /usr/share/nmap/scripts/imap-brute.nse	%{buildroot}/usr/share/nmap/scripts/imap-brute.nse
install -m 0755 /usr/share/nmap/scripts/imap-capabilities.nse	%{buildroot}/usr/share/nmap/scripts/imap-capabilities.nse
install -m 0755 /usr/share/nmap/scripts/imap-ntlm-info.nse	%{buildroot}/usr/share/nmap/scripts/imap-ntlm-info.nse
install -m 0755 /usr/share/nmap/scripts/impress-remote-discover.nse	%{buildroot}/usr/share/nmap/scripts/impress-remote-discover.nse
install -m 0755 /usr/share/nmap/scripts/informix-brute.nse	%{buildroot}/usr/share/nmap/scripts/informix-brute.nse
install -m 0755 /usr/share/nmap/scripts/informix-query.nse	%{buildroot}/usr/share/nmap/scripts/informix-query.nse
install -m 0755 /usr/share/nmap/scripts/informix-tables.nse	%{buildroot}/usr/share/nmap/scripts/informix-tables.nse
install -m 0755 /usr/share/nmap/scripts/ip-forwarding.nse	%{buildroot}/usr/share/nmap/scripts/ip-forwarding.nse
install -m 0755 /usr/share/nmap/scripts/ip-geolocation-geoplugin.nse	%{buildroot}/usr/share/nmap/scripts/ip-geolocation-geoplugin.nse
install -m 0755 /usr/share/nmap/scripts/ip-geolocation-ipinfodb.nse	%{buildroot}/usr/share/nmap/scripts/ip-geolocation-ipinfodb.nse
install -m 0755 /usr/share/nmap/scripts/ip-geolocation-map-bing.nse	%{buildroot}/usr/share/nmap/scripts/ip-geolocation-map-bing.nse
install -m 0755 /usr/share/nmap/scripts/ip-geolocation-map-google.nse	%{buildroot}/usr/share/nmap/scripts/ip-geolocation-map-google.nse
install -m 0755 /usr/share/nmap/scripts/ip-geolocation-map-kml.nse	%{buildroot}/usr/share/nmap/scripts/ip-geolocation-map-kml.nse
install -m 0755 /usr/share/nmap/scripts/ip-geolocation-maxmind.nse	%{buildroot}/usr/share/nmap/scripts/ip-geolocation-maxmind.nse
install -m 0755 /usr/share/nmap/scripts/ip-https-discover.nse	%{buildroot}/usr/share/nmap/scripts/ip-https-discover.nse
install -m 0755 /usr/share/nmap/scripts/ipidseq.nse	%{buildroot}/usr/share/nmap/scripts/ipidseq.nse
install -m 0755 /usr/share/nmap/scripts/ipmi-brute.nse	%{buildroot}/usr/share/nmap/scripts/ipmi-brute.nse
install -m 0755 /usr/share/nmap/scripts/ipmi-cipher-zero.nse	%{buildroot}/usr/share/nmap/scripts/ipmi-cipher-zero.nse
install -m 0755 /usr/share/nmap/scripts/ipmi-version.nse	%{buildroot}/usr/share/nmap/scripts/ipmi-version.nse
install -m 0755 /usr/share/nmap/scripts/ipv6-multicast-mld-list.nse	%{buildroot}/usr/share/nmap/scripts/ipv6-multicast-mld-list.nse
install -m 0755 /usr/share/nmap/scripts/ipv6-node-info.nse	%{buildroot}/usr/share/nmap/scripts/ipv6-node-info.nse
install -m 0755 /usr/share/nmap/scripts/ipv6-ra-flood.nse	%{buildroot}/usr/share/nmap/scripts/ipv6-ra-flood.nse
install -m 0755 /usr/share/nmap/scripts/irc-botnet-channels.nse	%{buildroot}/usr/share/nmap/scripts/irc-botnet-channels.nse
install -m 0755 /usr/share/nmap/scripts/irc-brute.nse	%{buildroot}/usr/share/nmap/scripts/irc-brute.nse
install -m 0755 /usr/share/nmap/scripts/irc-info.nse	%{buildroot}/usr/share/nmap/scripts/irc-info.nse
install -m 0755 /usr/share/nmap/scripts/irc-sasl-brute.nse	%{buildroot}/usr/share/nmap/scripts/irc-sasl-brute.nse
install -m 0755 /usr/share/nmap/scripts/irc-unrealircd-backdoor.nse	%{buildroot}/usr/share/nmap/scripts/irc-unrealircd-backdoor.nse
install -m 0755 /usr/share/nmap/scripts/iscsi-brute.nse	%{buildroot}/usr/share/nmap/scripts/iscsi-brute.nse
install -m 0755 /usr/share/nmap/scripts/iscsi-info.nse	%{buildroot}/usr/share/nmap/scripts/iscsi-info.nse
install -m 0755 /usr/share/nmap/scripts/isns-info.nse	%{buildroot}/usr/share/nmap/scripts/isns-info.nse
install -m 0755 /usr/share/nmap/scripts/jdwp-exec.nse	%{buildroot}/usr/share/nmap/scripts/jdwp-exec.nse
install -m 0755 /usr/share/nmap/scripts/jdwp-info.nse	%{buildroot}/usr/share/nmap/scripts/jdwp-info.nse
install -m 0755 /usr/share/nmap/scripts/jdwp-inject.nse	%{buildroot}/usr/share/nmap/scripts/jdwp-inject.nse
install -m 0755 /usr/share/nmap/scripts/jdwp-version.nse	%{buildroot}/usr/share/nmap/scripts/jdwp-version.nse
install -m 0755 /usr/share/nmap/scripts/knx-gateway-discover.nse	%{buildroot}/usr/share/nmap/scripts/knx-gateway-discover.nse
install -m 0755 /usr/share/nmap/scripts/knx-gateway-info.nse	%{buildroot}/usr/share/nmap/scripts/knx-gateway-info.nse
install -m 0755 /usr/share/nmap/scripts/krb5-enum-users.nse	%{buildroot}/usr/share/nmap/scripts/krb5-enum-users.nse
install -m 0755 /usr/share/nmap/scripts/ldap-brute.nse	%{buildroot}/usr/share/nmap/scripts/ldap-brute.nse
install -m 0755 /usr/share/nmap/scripts/ldap-novell-getpass.nse	%{buildroot}/usr/share/nmap/scripts/ldap-novell-getpass.nse
install -m 0755 /usr/share/nmap/scripts/ldap-rootdse.nse	%{buildroot}/usr/share/nmap/scripts/ldap-rootdse.nse
install -m 0755 /usr/share/nmap/scripts/ldap-search.nse	%{buildroot}/usr/share/nmap/scripts/ldap-search.nse
install -m 0755 /usr/share/nmap/scripts/lexmark-config.nse	%{buildroot}/usr/share/nmap/scripts/lexmark-config.nse
install -m 0755 /usr/share/nmap/scripts/llmnr-resolve.nse	%{buildroot}/usr/share/nmap/scripts/llmnr-resolve.nse
install -m 0755 /usr/share/nmap/scripts/lltd-discovery.nse	%{buildroot}/usr/share/nmap/scripts/lltd-discovery.nse
install -m 0755 /usr/share/nmap/scripts/lu-enum.nse	%{buildroot}/usr/share/nmap/scripts/lu-enum.nse
install -m 0755 /usr/share/nmap/scripts/maxdb-info.nse	%{buildroot}/usr/share/nmap/scripts/maxdb-info.nse
install -m 0755 /usr/share/nmap/scripts/mcafee-epo-agent.nse	%{buildroot}/usr/share/nmap/scripts/mcafee-epo-agent.nse
install -m 0755 /usr/share/nmap/scripts/membase-brute.nse	%{buildroot}/usr/share/nmap/scripts/membase-brute.nse
install -m 0755 /usr/share/nmap/scripts/membase-http-info.nse	%{buildroot}/usr/share/nmap/scripts/membase-http-info.nse
install -m 0755 /usr/share/nmap/scripts/memcached-info.nse	%{buildroot}/usr/share/nmap/scripts/memcached-info.nse
install -m 0755 /usr/share/nmap/scripts/metasploit-info.nse	%{buildroot}/usr/share/nmap/scripts/metasploit-info.nse
install -m 0755 /usr/share/nmap/scripts/metasploit-msgrpc-brute.nse	%{buildroot}/usr/share/nmap/scripts/metasploit-msgrpc-brute.nse
install -m 0755 /usr/share/nmap/scripts/metasploit-xmlrpc-brute.nse	%{buildroot}/usr/share/nmap/scripts/metasploit-xmlrpc-brute.nse
install -m 0755 /usr/share/nmap/scripts/mikrotik-routeros-brute.nse	%{buildroot}/usr/share/nmap/scripts/mikrotik-routeros-brute.nse
install -m 0755 /usr/share/nmap/scripts/mmouse-brute.nse	%{buildroot}/usr/share/nmap/scripts/mmouse-brute.nse
install -m 0755 /usr/share/nmap/scripts/mmouse-exec.nse	%{buildroot}/usr/share/nmap/scripts/mmouse-exec.nse
install -m 0755 /usr/share/nmap/scripts/modbus-discover.nse	%{buildroot}/usr/share/nmap/scripts/modbus-discover.nse
install -m 0755 /usr/share/nmap/scripts/mongodb-brute.nse	%{buildroot}/usr/share/nmap/scripts/mongodb-brute.nse
install -m 0755 /usr/share/nmap/scripts/mongodb-databases.nse	%{buildroot}/usr/share/nmap/scripts/mongodb-databases.nse
install -m 0755 /usr/share/nmap/scripts/mongodb-info.nse	%{buildroot}/usr/share/nmap/scripts/mongodb-info.nse
install -m 0755 /usr/share/nmap/scripts/mqtt-subscribe.nse	%{buildroot}/usr/share/nmap/scripts/mqtt-subscribe.nse
install -m 0755 /usr/share/nmap/scripts/mrinfo.nse	%{buildroot}/usr/share/nmap/scripts/mrinfo.nse
install -m 0755 /usr/share/nmap/scripts/ms-sql-brute.nse	%{buildroot}/usr/share/nmap/scripts/ms-sql-brute.nse
install -m 0755 /usr/share/nmap/scripts/ms-sql-config.nse	%{buildroot}/usr/share/nmap/scripts/ms-sql-config.nse
install -m 0755 /usr/share/nmap/scripts/ms-sql-dac.nse	%{buildroot}/usr/share/nmap/scripts/ms-sql-dac.nse
install -m 0755 /usr/share/nmap/scripts/ms-sql-dump-hashes.nse	%{buildroot}/usr/share/nmap/scripts/ms-sql-dump-hashes.nse
install -m 0755 /usr/share/nmap/scripts/ms-sql-empty-password.nse	%{buildroot}/usr/share/nmap/scripts/ms-sql-empty-password.nse
install -m 0755 /usr/share/nmap/scripts/ms-sql-hasdbaccess.nse	%{buildroot}/usr/share/nmap/scripts/ms-sql-hasdbaccess.nse
install -m 0755 /usr/share/nmap/scripts/ms-sql-info.nse	%{buildroot}/usr/share/nmap/scripts/ms-sql-info.nse
install -m 0755 /usr/share/nmap/scripts/ms-sql-ntlm-info.nse	%{buildroot}/usr/share/nmap/scripts/ms-sql-ntlm-info.nse
install -m 0755 /usr/share/nmap/scripts/ms-sql-query.nse	%{buildroot}/usr/share/nmap/scripts/ms-sql-query.nse
install -m 0755 /usr/share/nmap/scripts/ms-sql-tables.nse	%{buildroot}/usr/share/nmap/scripts/ms-sql-tables.nse
install -m 0755 /usr/share/nmap/scripts/ms-sql-xp-cmdshell.nse	%{buildroot}/usr/share/nmap/scripts/ms-sql-xp-cmdshell.nse
install -m 0755 /usr/share/nmap/scripts/msrpc-enum.nse	%{buildroot}/usr/share/nmap/scripts/msrpc-enum.nse
install -m 0755 /usr/share/nmap/scripts/mtrace.nse	%{buildroot}/usr/share/nmap/scripts/mtrace.nse
install -m 0755 /usr/share/nmap/scripts/murmur-version.nse	%{buildroot}/usr/share/nmap/scripts/murmur-version.nse
install -m 0755 /usr/share/nmap/scripts/mysql-audit.nse	%{buildroot}/usr/share/nmap/scripts/mysql-audit.nse
install -m 0755 /usr/share/nmap/scripts/mysql-brute.nse	%{buildroot}/usr/share/nmap/scripts/mysql-brute.nse
install -m 0755 /usr/share/nmap/scripts/mysql-databases.nse	%{buildroot}/usr/share/nmap/scripts/mysql-databases.nse
install -m 0755 /usr/share/nmap/scripts/mysql-dump-hashes.nse	%{buildroot}/usr/share/nmap/scripts/mysql-dump-hashes.nse
install -m 0755 /usr/share/nmap/scripts/mysql-empty-password.nse	%{buildroot}/usr/share/nmap/scripts/mysql-empty-password.nse
install -m 0755 /usr/share/nmap/scripts/mysql-enum.nse	%{buildroot}/usr/share/nmap/scripts/mysql-enum.nse
install -m 0755 /usr/share/nmap/scripts/mysql-info.nse	%{buildroot}/usr/share/nmap/scripts/mysql-info.nse
install -m 0755 /usr/share/nmap/scripts/mysql-query.nse	%{buildroot}/usr/share/nmap/scripts/mysql-query.nse
install -m 0755 /usr/share/nmap/scripts/mysql-users.nse	%{buildroot}/usr/share/nmap/scripts/mysql-users.nse
install -m 0755 /usr/share/nmap/scripts/mysql-variables.nse	%{buildroot}/usr/share/nmap/scripts/mysql-variables.nse
install -m 0755 /usr/share/nmap/scripts/mysql-vuln-cve2012-2122.nse	%{buildroot}/usr/share/nmap/scripts/mysql-vuln-cve2012-2122.nse
install -m 0755 /usr/share/nmap/scripts/nat-pmp-info.nse	%{buildroot}/usr/share/nmap/scripts/nat-pmp-info.nse
install -m 0755 /usr/share/nmap/scripts/nat-pmp-mapport.nse	%{buildroot}/usr/share/nmap/scripts/nat-pmp-mapport.nse
install -m 0755 /usr/share/nmap/scripts/nbd-info.nse	%{buildroot}/usr/share/nmap/scripts/nbd-info.nse
install -m 0755 /usr/share/nmap/scripts/nbstat.nse	%{buildroot}/usr/share/nmap/scripts/nbstat.nse
install -m 0755 /usr/share/nmap/scripts/ncp-enum-users.nse	%{buildroot}/usr/share/nmap/scripts/ncp-enum-users.nse
install -m 0755 /usr/share/nmap/scripts/ncp-serverinfo.nse	%{buildroot}/usr/share/nmap/scripts/ncp-serverinfo.nse
install -m 0755 /usr/share/nmap/scripts/ndmp-fs-info.nse	%{buildroot}/usr/share/nmap/scripts/ndmp-fs-info.nse
install -m 0755 /usr/share/nmap/scripts/ndmp-version.nse	%{buildroot}/usr/share/nmap/scripts/ndmp-version.nse
install -m 0755 /usr/share/nmap/scripts/nessus-brute.nse	%{buildroot}/usr/share/nmap/scripts/nessus-brute.nse
install -m 0755 /usr/share/nmap/scripts/nessus-xmlrpc-brute.nse	%{buildroot}/usr/share/nmap/scripts/nessus-xmlrpc-brute.nse
install -m 0755 /usr/share/nmap/scripts/netbus-auth-bypass.nse	%{buildroot}/usr/share/nmap/scripts/netbus-auth-bypass.nse
install -m 0755 /usr/share/nmap/scripts/netbus-brute.nse	%{buildroot}/usr/share/nmap/scripts/netbus-brute.nse
install -m 0755 /usr/share/nmap/scripts/netbus-info.nse	%{buildroot}/usr/share/nmap/scripts/netbus-info.nse
install -m 0755 /usr/share/nmap/scripts/netbus-version.nse	%{buildroot}/usr/share/nmap/scripts/netbus-version.nse
install -m 0755 /usr/share/nmap/scripts/nexpose-brute.nse	%{buildroot}/usr/share/nmap/scripts/nexpose-brute.nse
install -m 0755 /usr/share/nmap/scripts/nfs-ls.nse	%{buildroot}/usr/share/nmap/scripts/nfs-ls.nse
install -m 0755 /usr/share/nmap/scripts/nfs-showmount.nse	%{buildroot}/usr/share/nmap/scripts/nfs-showmount.nse
install -m 0755 /usr/share/nmap/scripts/nfs-statfs.nse	%{buildroot}/usr/share/nmap/scripts/nfs-statfs.nse
install -m 0755 /usr/share/nmap/scripts/nje-node-brute.nse	%{buildroot}/usr/share/nmap/scripts/nje-node-brute.nse
install -m 0755 /usr/share/nmap/scripts/nje-pass-brute.nse	%{buildroot}/usr/share/nmap/scripts/nje-pass-brute.nse
install -m 0755 /usr/share/nmap/scripts/nntp-ntlm-info.nse	%{buildroot}/usr/share/nmap/scripts/nntp-ntlm-info.nse
install -m 0755 /usr/share/nmap/scripts/nping-brute.nse	%{buildroot}/usr/share/nmap/scripts/nping-brute.nse
install -m 0755 /usr/share/nmap/scripts/nrpe-enum.nse	%{buildroot}/usr/share/nmap/scripts/nrpe-enum.nse
install -m 0755 /usr/share/nmap/scripts/ntp-info.nse	%{buildroot}/usr/share/nmap/scripts/ntp-info.nse
install -m 0755 /usr/share/nmap/scripts/ntp-monlist.nse	%{buildroot}/usr/share/nmap/scripts/ntp-monlist.nse
install -m 0755 /usr/share/nmap/scripts/omp2-brute.nse	%{buildroot}/usr/share/nmap/scripts/omp2-brute.nse
install -m 0755 /usr/share/nmap/scripts/omp2-enum-targets.nse	%{buildroot}/usr/share/nmap/scripts/omp2-enum-targets.nse
install -m 0755 /usr/share/nmap/scripts/omron-info.nse	%{buildroot}/usr/share/nmap/scripts/omron-info.nse
install -m 0755 /usr/share/nmap/scripts/openlookup-info.nse	%{buildroot}/usr/share/nmap/scripts/openlookup-info.nse
install -m 0755 /usr/share/nmap/scripts/openvas-otp-brute.nse	%{buildroot}/usr/share/nmap/scripts/openvas-otp-brute.nse
install -m 0755 /usr/share/nmap/scripts/openwebnet-discovery.nse	%{buildroot}/usr/share/nmap/scripts/openwebnet-discovery.nse
install -m 0755 /usr/share/nmap/scripts/oracle-brute-stealth.nse	%{buildroot}/usr/share/nmap/scripts/oracle-brute-stealth.nse
install -m 0755 /usr/share/nmap/scripts/oracle-brute.nse	%{buildroot}/usr/share/nmap/scripts/oracle-brute.nse
install -m 0755 /usr/share/nmap/scripts/oracle-enum-users.nse	%{buildroot}/usr/share/nmap/scripts/oracle-enum-users.nse
install -m 0755 /usr/share/nmap/scripts/oracle-sid-brute.nse	%{buildroot}/usr/share/nmap/scripts/oracle-sid-brute.nse
install -m 0755 /usr/share/nmap/scripts/oracle-tns-version.nse	%{buildroot}/usr/share/nmap/scripts/oracle-tns-version.nse
install -m 0755 /usr/share/nmap/scripts/ovs-agent-version.nse	%{buildroot}/usr/share/nmap/scripts/ovs-agent-version.nse
install -m 0755 /usr/share/nmap/scripts/p2p-conficker.nse	%{buildroot}/usr/share/nmap/scripts/p2p-conficker.nse
install -m 0755 /usr/share/nmap/scripts/path-mtu.nse	%{buildroot}/usr/share/nmap/scripts/path-mtu.nse
install -m 0755 /usr/share/nmap/scripts/pcanywhere-brute.nse	%{buildroot}/usr/share/nmap/scripts/pcanywhere-brute.nse
install -m 0755 /usr/share/nmap/scripts/pcworx-info.nse	%{buildroot}/usr/share/nmap/scripts/pcworx-info.nse
install -m 0755 /usr/share/nmap/scripts/pgsql-brute.nse	%{buildroot}/usr/share/nmap/scripts/pgsql-brute.nse
install -m 0755 /usr/share/nmap/scripts/pjl-ready-message.nse	%{buildroot}/usr/share/nmap/scripts/pjl-ready-message.nse
install -m 0755 /usr/share/nmap/scripts/pop3-brute.nse	%{buildroot}/usr/share/nmap/scripts/pop3-brute.nse
install -m 0755 /usr/share/nmap/scripts/pop3-capabilities.nse	%{buildroot}/usr/share/nmap/scripts/pop3-capabilities.nse
install -m 0755 /usr/share/nmap/scripts/pop3-ntlm-info.nse	%{buildroot}/usr/share/nmap/scripts/pop3-ntlm-info.nse
install -m 0755 /usr/share/nmap/scripts/pptp-version.nse	%{buildroot}/usr/share/nmap/scripts/pptp-version.nse
install -m 0755 /usr/share/nmap/scripts/puppet-naivesigning.nse	%{buildroot}/usr/share/nmap/scripts/puppet-naivesigning.nse
install -m 0755 /usr/share/nmap/scripts/qconn-exec.nse	%{buildroot}/usr/share/nmap/scripts/qconn-exec.nse
install -m 0755 /usr/share/nmap/scripts/qscan.nse	%{buildroot}/usr/share/nmap/scripts/qscan.nse
install -m 0755 /usr/share/nmap/scripts/quake1-info.nse	%{buildroot}/usr/share/nmap/scripts/quake1-info.nse
install -m 0755 /usr/share/nmap/scripts/quake3-info.nse	%{buildroot}/usr/share/nmap/scripts/quake3-info.nse
install -m 0755 /usr/share/nmap/scripts/quake3-master-getservers.nse	%{buildroot}/usr/share/nmap/scripts/quake3-master-getservers.nse
install -m 0755 /usr/share/nmap/scripts/rdp-enum-encryption.nse	%{buildroot}/usr/share/nmap/scripts/rdp-enum-encryption.nse
install -m 0755 /usr/share/nmap/scripts/rdp-ntlm-info.nse	%{buildroot}/usr/share/nmap/scripts/rdp-ntlm-info.nse
install -m 0755 /usr/share/nmap/scripts/rdp-vuln-ms12-020.nse	%{buildroot}/usr/share/nmap/scripts/rdp-vuln-ms12-020.nse
install -m 0755 /usr/share/nmap/scripts/realvnc-auth-bypass.nse	%{buildroot}/usr/share/nmap/scripts/realvnc-auth-bypass.nse
install -m 0755 /usr/share/nmap/scripts/redis-brute.nse	%{buildroot}/usr/share/nmap/scripts/redis-brute.nse
install -m 0755 /usr/share/nmap/scripts/redis-info.nse	%{buildroot}/usr/share/nmap/scripts/redis-info.nse
install -m 0755 /usr/share/nmap/scripts/resolveall.nse	%{buildroot}/usr/share/nmap/scripts/resolveall.nse
install -m 0755 /usr/share/nmap/scripts/reverse-index.nse	%{buildroot}/usr/share/nmap/scripts/reverse-index.nse
install -m 0755 /usr/share/nmap/scripts/rexec-brute.nse	%{buildroot}/usr/share/nmap/scripts/rexec-brute.nse
install -m 0755 /usr/share/nmap/scripts/rfc868-time.nse	%{buildroot}/usr/share/nmap/scripts/rfc868-time.nse
install -m 0755 /usr/share/nmap/scripts/riak-http-info.nse	%{buildroot}/usr/share/nmap/scripts/riak-http-info.nse
install -m 0755 /usr/share/nmap/scripts/rlogin-brute.nse	%{buildroot}/usr/share/nmap/scripts/rlogin-brute.nse
install -m 0755 /usr/share/nmap/scripts/rmi-dumpregistry.nse	%{buildroot}/usr/share/nmap/scripts/rmi-dumpregistry.nse
install -m 0755 /usr/share/nmap/scripts/rmi-vuln-classloader.nse	%{buildroot}/usr/share/nmap/scripts/rmi-vuln-classloader.nse
install -m 0755 /usr/share/nmap/scripts/rpc-grind.nse	%{buildroot}/usr/share/nmap/scripts/rpc-grind.nse
install -m 0755 /usr/share/nmap/scripts/rpcap-brute.nse	%{buildroot}/usr/share/nmap/scripts/rpcap-brute.nse
install -m 0755 /usr/share/nmap/scripts/rpcap-info.nse	%{buildroot}/usr/share/nmap/scripts/rpcap-info.nse
install -m 0755 /usr/share/nmap/scripts/rpcinfo.nse	%{buildroot}/usr/share/nmap/scripts/rpcinfo.nse
install -m 0755 /usr/share/nmap/scripts/rsa-vuln-roca.nse	%{buildroot}/usr/share/nmap/scripts/rsa-vuln-roca.nse
install -m 0755 /usr/share/nmap/scripts/rsync-brute.nse	%{buildroot}/usr/share/nmap/scripts/rsync-brute.nse
install -m 0755 /usr/share/nmap/scripts/rsync-list-modules.nse	%{buildroot}/usr/share/nmap/scripts/rsync-list-modules.nse
install -m 0755 /usr/share/nmap/scripts/rtsp-methods.nse	%{buildroot}/usr/share/nmap/scripts/rtsp-methods.nse
install -m 0755 /usr/share/nmap/scripts/rtsp-url-brute.nse	%{buildroot}/usr/share/nmap/scripts/rtsp-url-brute.nse
install -m 0755 /usr/share/nmap/scripts/rusers.nse	%{buildroot}/usr/share/nmap/scripts/rusers.nse
install -m 0755 /usr/share/nmap/scripts/s7-info.nse	%{buildroot}/usr/share/nmap/scripts/s7-info.nse
install -m 0755 /usr/share/nmap/scripts/samba-vuln-cve-2012-1182.nse	%{buildroot}/usr/share/nmap/scripts/samba-vuln-cve-2012-1182.nse
install -m 0755 /usr/share/nmap/scripts/script.db	%{buildroot}/usr/share/nmap/scripts/script.db
install -m 0755 /usr/share/nmap/scripts/servicetags.nse	%{buildroot}/usr/share/nmap/scripts/servicetags.nse
install -m 0755 /usr/share/nmap/scripts/shodan-api.nse	%{buildroot}/usr/share/nmap/scripts/shodan-api.nse
install -m 0755 /usr/share/nmap/scripts/sip-brute.nse	%{buildroot}/usr/share/nmap/scripts/sip-brute.nse
install -m 0755 /usr/share/nmap/scripts/sip-call-spoof.nse	%{buildroot}/usr/share/nmap/scripts/sip-call-spoof.nse
install -m 0755 /usr/share/nmap/scripts/sip-enum-users.nse	%{buildroot}/usr/share/nmap/scripts/sip-enum-users.nse
install -m 0755 /usr/share/nmap/scripts/sip-methods.nse	%{buildroot}/usr/share/nmap/scripts/sip-methods.nse
install -m 0755 /usr/share/nmap/scripts/skypev2-version.nse	%{buildroot}/usr/share/nmap/scripts/skypev2-version.nse
install -m 0755 /usr/share/nmap/scripts/smb-brute.nse	%{buildroot}/usr/share/nmap/scripts/smb-brute.nse
install -m 0755 /usr/share/nmap/scripts/smb-double-pulsar-backdoor.nse	%{buildroot}/usr/share/nmap/scripts/smb-double-pulsar-backdoor.nse
install -m 0755 /usr/share/nmap/scripts/smb-enum-domains.nse	%{buildroot}/usr/share/nmap/scripts/smb-enum-domains.nse
install -m 0755 /usr/share/nmap/scripts/smb-enum-groups.nse	%{buildroot}/usr/share/nmap/scripts/smb-enum-groups.nse
install -m 0755 /usr/share/nmap/scripts/smb-enum-processes.nse	%{buildroot}/usr/share/nmap/scripts/smb-enum-processes.nse
install -m 0755 /usr/share/nmap/scripts/smb-enum-services.nse	%{buildroot}/usr/share/nmap/scripts/smb-enum-services.nse
install -m 0755 /usr/share/nmap/scripts/smb-enum-sessions.nse	%{buildroot}/usr/share/nmap/scripts/smb-enum-sessions.nse
install -m 0755 /usr/share/nmap/scripts/smb-enum-shares.nse	%{buildroot}/usr/share/nmap/scripts/smb-enum-shares.nse
install -m 0755 /usr/share/nmap/scripts/smb-enum-users.nse	%{buildroot}/usr/share/nmap/scripts/smb-enum-users.nse
install -m 0755 /usr/share/nmap/scripts/smb-flood.nse	%{buildroot}/usr/share/nmap/scripts/smb-flood.nse
install -m 0755 /usr/share/nmap/scripts/smb-ls.nse	%{buildroot}/usr/share/nmap/scripts/smb-ls.nse
install -m 0755 /usr/share/nmap/scripts/smb-mbenum.nse	%{buildroot}/usr/share/nmap/scripts/smb-mbenum.nse
install -m 0755 /usr/share/nmap/scripts/smb-os-discovery.nse	%{buildroot}/usr/share/nmap/scripts/smb-os-discovery.nse
install -m 0755 /usr/share/nmap/scripts/smb-print-text.nse	%{buildroot}/usr/share/nmap/scripts/smb-print-text.nse
install -m 0755 /usr/share/nmap/scripts/smb-protocols.nse	%{buildroot}/usr/share/nmap/scripts/smb-protocols.nse
install -m 0755 /usr/share/nmap/scripts/smb-psexec.nse	%{buildroot}/usr/share/nmap/scripts/smb-psexec.nse
install -m 0755 /usr/share/nmap/scripts/smb-security-mode.nse	%{buildroot}/usr/share/nmap/scripts/smb-security-mode.nse
install -m 0755 /usr/share/nmap/scripts/smb-server-stats.nse	%{buildroot}/usr/share/nmap/scripts/smb-server-stats.nse
install -m 0755 /usr/share/nmap/scripts/smb-system-info.nse	%{buildroot}/usr/share/nmap/scripts/smb-system-info.nse
install -m 0755 /usr/share/nmap/scripts/smb-vuln-conficker.nse	%{buildroot}/usr/share/nmap/scripts/smb-vuln-conficker.nse
install -m 0755 /usr/share/nmap/scripts/smb-vuln-cve-2017-7494.nse	%{buildroot}/usr/share/nmap/scripts/smb-vuln-cve-2017-7494.nse
install -m 0755 /usr/share/nmap/scripts/smb-vuln-cve2009-3103.nse	%{buildroot}/usr/share/nmap/scripts/smb-vuln-cve2009-3103.nse
install -m 0755 /usr/share/nmap/scripts/smb-vuln-ms06-025.nse	%{buildroot}/usr/share/nmap/scripts/smb-vuln-ms06-025.nse
install -m 0755 /usr/share/nmap/scripts/smb-vuln-ms07-029.nse	%{buildroot}/usr/share/nmap/scripts/smb-vuln-ms07-029.nse
install -m 0755 /usr/share/nmap/scripts/smb-vuln-ms08-067.nse	%{buildroot}/usr/share/nmap/scripts/smb-vuln-ms08-067.nse
install -m 0755 /usr/share/nmap/scripts/smb-vuln-ms10-054.nse	%{buildroot}/usr/share/nmap/scripts/smb-vuln-ms10-054.nse
install -m 0755 /usr/share/nmap/scripts/smb-vuln-ms10-061.nse	%{buildroot}/usr/share/nmap/scripts/smb-vuln-ms10-061.nse
install -m 0755 /usr/share/nmap/scripts/smb-vuln-ms17-010.nse	%{buildroot}/usr/share/nmap/scripts/smb-vuln-ms17-010.nse
install -m 0755 /usr/share/nmap/scripts/smb-vuln-regsvc-dos.nse	%{buildroot}/usr/share/nmap/scripts/smb-vuln-regsvc-dos.nse
install -m 0755 /usr/share/nmap/scripts/smb-vuln-webexec.nse	%{buildroot}/usr/share/nmap/scripts/smb-vuln-webexec.nse
install -m 0755 /usr/share/nmap/scripts/smb-webexec-exploit.nse	%{buildroot}/usr/share/nmap/scripts/smb-webexec-exploit.nse
install -m 0755 /usr/share/nmap/scripts/smb2-capabilities.nse	%{buildroot}/usr/share/nmap/scripts/smb2-capabilities.nse
install -m 0755 /usr/share/nmap/scripts/smb2-security-mode.nse	%{buildroot}/usr/share/nmap/scripts/smb2-security-mode.nse
install -m 0755 /usr/share/nmap/scripts/smb2-time.nse	%{buildroot}/usr/share/nmap/scripts/smb2-time.nse
install -m 0755 /usr/share/nmap/scripts/smb2-vuln-uptime.nse	%{buildroot}/usr/share/nmap/scripts/smb2-vuln-uptime.nse
install -m 0755 /usr/share/nmap/scripts/smtp-brute.nse	%{buildroot}/usr/share/nmap/scripts/smtp-brute.nse
install -m 0755 /usr/share/nmap/scripts/smtp-commands.nse	%{buildroot}/usr/share/nmap/scripts/smtp-commands.nse
install -m 0755 /usr/share/nmap/scripts/smtp-enum-users.nse	%{buildroot}/usr/share/nmap/scripts/smtp-enum-users.nse
install -m 0755 /usr/share/nmap/scripts/smtp-ntlm-info.nse	%{buildroot}/usr/share/nmap/scripts/smtp-ntlm-info.nse
install -m 0755 /usr/share/nmap/scripts/smtp-open-relay.nse	%{buildroot}/usr/share/nmap/scripts/smtp-open-relay.nse
install -m 0755 /usr/share/nmap/scripts/smtp-strangeport.nse	%{buildroot}/usr/share/nmap/scripts/smtp-strangeport.nse
install -m 0755 /usr/share/nmap/scripts/smtp-vuln-cve2010-4344.nse	%{buildroot}/usr/share/nmap/scripts/smtp-vuln-cve2010-4344.nse
install -m 0755 /usr/share/nmap/scripts/smtp-vuln-cve2011-1720.nse	%{buildroot}/usr/share/nmap/scripts/smtp-vuln-cve2011-1720.nse
install -m 0755 /usr/share/nmap/scripts/smtp-vuln-cve2011-1764.nse	%{buildroot}/usr/share/nmap/scripts/smtp-vuln-cve2011-1764.nse
install -m 0755 /usr/share/nmap/scripts/sniffer-detect.nse	%{buildroot}/usr/share/nmap/scripts/sniffer-detect.nse
install -m 0755 /usr/share/nmap/scripts/snmp-brute.nse	%{buildroot}/usr/share/nmap/scripts/snmp-brute.nse
install -m 0755 /usr/share/nmap/scripts/snmp-hh3c-logins.nse	%{buildroot}/usr/share/nmap/scripts/snmp-hh3c-logins.nse
install -m 0755 /usr/share/nmap/scripts/snmp-info.nse	%{buildroot}/usr/share/nmap/scripts/snmp-info.nse
install -m 0755 /usr/share/nmap/scripts/snmp-interfaces.nse	%{buildroot}/usr/share/nmap/scripts/snmp-interfaces.nse
install -m 0755 /usr/share/nmap/scripts/snmp-ios-config.nse	%{buildroot}/usr/share/nmap/scripts/snmp-ios-config.nse
install -m 0755 /usr/share/nmap/scripts/snmp-netstat.nse	%{buildroot}/usr/share/nmap/scripts/snmp-netstat.nse
install -m 0755 /usr/share/nmap/scripts/snmp-processes.nse	%{buildroot}/usr/share/nmap/scripts/snmp-processes.nse
install -m 0755 /usr/share/nmap/scripts/snmp-sysdescr.nse	%{buildroot}/usr/share/nmap/scripts/snmp-sysdescr.nse
install -m 0755 /usr/share/nmap/scripts/snmp-win32-services.nse	%{buildroot}/usr/share/nmap/scripts/snmp-win32-services.nse
install -m 0755 /usr/share/nmap/scripts/snmp-win32-shares.nse	%{buildroot}/usr/share/nmap/scripts/snmp-win32-shares.nse
install -m 0755 /usr/share/nmap/scripts/snmp-win32-software.nse	%{buildroot}/usr/share/nmap/scripts/snmp-win32-software.nse
install -m 0755 /usr/share/nmap/scripts/snmp-win32-users.nse	%{buildroot}/usr/share/nmap/scripts/snmp-win32-users.nse
install -m 0755 /usr/share/nmap/scripts/socks-auth-info.nse	%{buildroot}/usr/share/nmap/scripts/socks-auth-info.nse
install -m 0755 /usr/share/nmap/scripts/socks-brute.nse	%{buildroot}/usr/share/nmap/scripts/socks-brute.nse
install -m 0755 /usr/share/nmap/scripts/socks-open-proxy.nse	%{buildroot}/usr/share/nmap/scripts/socks-open-proxy.nse
install -m 0755 /usr/share/nmap/scripts/ssh-auth-methods.nse	%{buildroot}/usr/share/nmap/scripts/ssh-auth-methods.nse
install -m 0755 /usr/share/nmap/scripts/ssh-brute.nse	%{buildroot}/usr/share/nmap/scripts/ssh-brute.nse
install -m 0755 /usr/share/nmap/scripts/ssh-hostkey.nse	%{buildroot}/usr/share/nmap/scripts/ssh-hostkey.nse
install -m 0755 /usr/share/nmap/scripts/ssh-publickey-acceptance.nse	%{buildroot}/usr/share/nmap/scripts/ssh-publickey-acceptance.nse
install -m 0755 /usr/share/nmap/scripts/ssh-run.nse	%{buildroot}/usr/share/nmap/scripts/ssh-run.nse
install -m 0755 /usr/share/nmap/scripts/ssh2-enum-algos.nse	%{buildroot}/usr/share/nmap/scripts/ssh2-enum-algos.nse
install -m 0755 /usr/share/nmap/scripts/sshv1.nse	%{buildroot}/usr/share/nmap/scripts/sshv1.nse
install -m 0755 /usr/share/nmap/scripts/ssl-ccs-injection.nse	%{buildroot}/usr/share/nmap/scripts/ssl-ccs-injection.nse
install -m 0755 /usr/share/nmap/scripts/ssl-cert-intaddr.nse	%{buildroot}/usr/share/nmap/scripts/ssl-cert-intaddr.nse
install -m 0755 /usr/share/nmap/scripts/ssl-cert.nse	%{buildroot}/usr/share/nmap/scripts/ssl-cert.nse
install -m 0755 /usr/share/nmap/scripts/ssl-date.nse	%{buildroot}/usr/share/nmap/scripts/ssl-date.nse
install -m 0755 /usr/share/nmap/scripts/ssl-dh-params.nse	%{buildroot}/usr/share/nmap/scripts/ssl-dh-params.nse
install -m 0755 /usr/share/nmap/scripts/ssl-enum-ciphers.nse	%{buildroot}/usr/share/nmap/scripts/ssl-enum-ciphers.nse
install -m 0755 /usr/share/nmap/scripts/ssl-heartbleed.nse	%{buildroot}/usr/share/nmap/scripts/ssl-heartbleed.nse
install -m 0755 /usr/share/nmap/scripts/ssl-known-key.nse	%{buildroot}/usr/share/nmap/scripts/ssl-known-key.nse
install -m 0755 /usr/share/nmap/scripts/ssl-poodle.nse	%{buildroot}/usr/share/nmap/scripts/ssl-poodle.nse
install -m 0755 /usr/share/nmap/scripts/sslv2-drown.nse	%{buildroot}/usr/share/nmap/scripts/sslv2-drown.nse
install -m 0755 /usr/share/nmap/scripts/sslv2.nse	%{buildroot}/usr/share/nmap/scripts/sslv2.nse
install -m 0755 /usr/share/nmap/scripts/sstp-discover.nse	%{buildroot}/usr/share/nmap/scripts/sstp-discover.nse
install -m 0755 /usr/share/nmap/scripts/stun-info.nse	%{buildroot}/usr/share/nmap/scripts/stun-info.nse
install -m 0755 /usr/share/nmap/scripts/stun-version.nse	%{buildroot}/usr/share/nmap/scripts/stun-version.nse
install -m 0755 /usr/share/nmap/scripts/stuxnet-detect.nse	%{buildroot}/usr/share/nmap/scripts/stuxnet-detect.nse
install -m 0755 /usr/share/nmap/scripts/supermicro-ipmi-conf.nse	%{buildroot}/usr/share/nmap/scripts/supermicro-ipmi-conf.nse
install -m 0755 /usr/share/nmap/scripts/svn-brute.nse	%{buildroot}/usr/share/nmap/scripts/svn-brute.nse
install -m 0755 /usr/share/nmap/scripts/targets-asn.nse	%{buildroot}/usr/share/nmap/scripts/targets-asn.nse
install -m 0755 /usr/share/nmap/scripts/targets-ipv6-map4to6.nse	%{buildroot}/usr/share/nmap/scripts/targets-ipv6-map4to6.nse
install -m 0755 /usr/share/nmap/scripts/targets-ipv6-multicast-echo.nse	%{buildroot}/usr/share/nmap/scripts/targets-ipv6-multicast-echo.nse
install -m 0755 /usr/share/nmap/scripts/targets-ipv6-multicast-invalid-dst.nse	%{buildroot}/usr/share/nmap/scripts/targets-ipv6-multicast-invalid-dst.nse
install -m 0755 /usr/share/nmap/scripts/targets-ipv6-multicast-mld.nse	%{buildroot}/usr/share/nmap/scripts/targets-ipv6-multicast-mld.nse
install -m 0755 /usr/share/nmap/scripts/targets-ipv6-multicast-slaac.nse	%{buildroot}/usr/share/nmap/scripts/targets-ipv6-multicast-slaac.nse
install -m 0755 /usr/share/nmap/scripts/targets-ipv6-wordlist.nse	%{buildroot}/usr/share/nmap/scripts/targets-ipv6-wordlist.nse
install -m 0755 /usr/share/nmap/scripts/targets-sniffer.nse	%{buildroot}/usr/share/nmap/scripts/targets-sniffer.nse
install -m 0755 /usr/share/nmap/scripts/targets-traceroute.nse	%{buildroot}/usr/share/nmap/scripts/targets-traceroute.nse
install -m 0755 /usr/share/nmap/scripts/targets-xml.nse	%{buildroot}/usr/share/nmap/scripts/targets-xml.nse
install -m 0755 /usr/share/nmap/scripts/teamspeak2-version.nse	%{buildroot}/usr/share/nmap/scripts/teamspeak2-version.nse
install -m 0755 /usr/share/nmap/scripts/telnet-brute.nse	%{buildroot}/usr/share/nmap/scripts/telnet-brute.nse
install -m 0755 /usr/share/nmap/scripts/telnet-encryption.nse	%{buildroot}/usr/share/nmap/scripts/telnet-encryption.nse
install -m 0755 /usr/share/nmap/scripts/telnet-ntlm-info.nse	%{buildroot}/usr/share/nmap/scripts/telnet-ntlm-info.nse
install -m 0755 /usr/share/nmap/scripts/tftp-enum.nse	%{buildroot}/usr/share/nmap/scripts/tftp-enum.nse
install -m 0755 /usr/share/nmap/scripts/tls-alpn.nse	%{buildroot}/usr/share/nmap/scripts/tls-alpn.nse
install -m 0755 /usr/share/nmap/scripts/tls-nextprotoneg.nse	%{buildroot}/usr/share/nmap/scripts/tls-nextprotoneg.nse
install -m 0755 /usr/share/nmap/scripts/tls-ticketbleed.nse	%{buildroot}/usr/share/nmap/scripts/tls-ticketbleed.nse
install -m 0755 /usr/share/nmap/scripts/tn3270-screen.nse	%{buildroot}/usr/share/nmap/scripts/tn3270-screen.nse
install -m 0755 /usr/share/nmap/scripts/tor-consensus-checker.nse	%{buildroot}/usr/share/nmap/scripts/tor-consensus-checker.nse
install -m 0755 /usr/share/nmap/scripts/traceroute-geolocation.nse	%{buildroot}/usr/share/nmap/scripts/traceroute-geolocation.nse
install -m 0755 /usr/share/nmap/scripts/tso-brute.nse	%{buildroot}/usr/share/nmap/scripts/tso-brute.nse
install -m 0755 /usr/share/nmap/scripts/tso-enum.nse	%{buildroot}/usr/share/nmap/scripts/tso-enum.nse
install -m 0755 /usr/share/nmap/scripts/ubiquiti-discovery.nse	%{buildroot}/usr/share/nmap/scripts/ubiquiti-discovery.nse
install -m 0755 /usr/share/nmap/scripts/unittest.nse	%{buildroot}/usr/share/nmap/scripts/unittest.nse
install -m 0755 /usr/share/nmap/scripts/unusual-port.nse	%{buildroot}/usr/share/nmap/scripts/unusual-port.nse
install -m 0755 /usr/share/nmap/scripts/upnp-info.nse	%{buildroot}/usr/share/nmap/scripts/upnp-info.nse
install -m 0755 /usr/share/nmap/scripts/url-snarf.nse	%{buildroot}/usr/share/nmap/scripts/url-snarf.nse
install -m 0755 /usr/share/nmap/scripts/ventrilo-info.nse	%{buildroot}/usr/share/nmap/scripts/ventrilo-info.nse
install -m 0755 /usr/share/nmap/scripts/versant-info.nse	%{buildroot}/usr/share/nmap/scripts/versant-info.nse
install -m 0755 /usr/share/nmap/scripts/vmauthd-brute.nse	%{buildroot}/usr/share/nmap/scripts/vmauthd-brute.nse
install -m 0755 /usr/share/nmap/scripts/vmware-version.nse	%{buildroot}/usr/share/nmap/scripts/vmware-version.nse
install -m 0755 /usr/share/nmap/scripts/vnc-brute.nse	%{buildroot}/usr/share/nmap/scripts/vnc-brute.nse
install -m 0755 /usr/share/nmap/scripts/vnc-info.nse	%{buildroot}/usr/share/nmap/scripts/vnc-info.nse
install -m 0755 /usr/share/nmap/scripts/vnc-title.nse	%{buildroot}/usr/share/nmap/scripts/vnc-title.nse
install -m 0755 /usr/share/nmap/scripts/voldemort-info.nse	%{buildroot}/usr/share/nmap/scripts/voldemort-info.nse
install -m 0755 /usr/share/nmap/scripts/vtam-enum.nse	%{buildroot}/usr/share/nmap/scripts/vtam-enum.nse
install -m 0755 /usr/share/nmap/scripts/vulners.nse	%{buildroot}/usr/share/nmap/scripts/vulners.nse
install -m 0755 /usr/share/nmap/scripts/vuze-dht-info.nse	%{buildroot}/usr/share/nmap/scripts/vuze-dht-info.nse
install -m 0755 /usr/share/nmap/scripts/wdb-version.nse	%{buildroot}/usr/share/nmap/scripts/wdb-version.nse
install -m 0755 /usr/share/nmap/scripts/weblogic-t3-info.nse	%{buildroot}/usr/share/nmap/scripts/weblogic-t3-info.nse
install -m 0755 /usr/share/nmap/scripts/whois-domain.nse	%{buildroot}/usr/share/nmap/scripts/whois-domain.nse
install -m 0755 /usr/share/nmap/scripts/whois-ip.nse	%{buildroot}/usr/share/nmap/scripts/whois-ip.nse
install -m 0755 /usr/share/nmap/scripts/wsdd-discover.nse	%{buildroot}/usr/share/nmap/scripts/wsdd-discover.nse
install -m 0755 /usr/share/nmap/scripts/x11-access.nse	%{buildroot}/usr/share/nmap/scripts/x11-access.nse
install -m 0755 /usr/share/nmap/scripts/xdmcp-discover.nse	%{buildroot}/usr/share/nmap/scripts/xdmcp-discover.nse
install -m 0755 /usr/share/nmap/scripts/xmlrpc-methods.nse	%{buildroot}/usr/share/nmap/scripts/xmlrpc-methods.nse
install -m 0755 /usr/share/nmap/scripts/xmpp-brute.nse	%{buildroot}/usr/share/nmap/scripts/xmpp-brute.nse
install -m 0755 /usr/share/nmap/scripts/xmpp-info.nse	%{buildroot}/usr/share/nmap/scripts/xmpp-info.nse
install -m 0755 /usr/share/zenmap/config/scan_profile.usp	%{buildroot}/usr/share/zenmap/config/scan_profile.usp
install -m 0755 /usr/share/zenmap/config/zenmap.conf	%{buildroot}/usr/share/zenmap/config/zenmap.conf
install -m 0755 /usr/share/zenmap/config/zenmap_version	%{buildroot}/usr/share/zenmap/config/zenmap_version
install -m 0755 /usr/share/zenmap/docs/help.html	%{buildroot}/usr/share/zenmap/docs/help.html
install -m 0755 /usr/share/zenmap/locale/de/LC_MESSAGES/zenmap.mo	%{buildroot}/usr/share/zenmap/locale/de/LC_MESSAGES/zenmap.mo
install -m 0755 /usr/share/zenmap/locale/es/LC_MESSAGES/zenmap.mo	%{buildroot}/usr/share/zenmap/locale/es/LC_MESSAGES/zenmap.mo
install -m 0755 /usr/share/zenmap/locale/fr/LC_MESSAGES/zenmap.mo	%{buildroot}/usr/share/zenmap/locale/fr/LC_MESSAGES/zenmap.mo
install -m 0755 /usr/share/zenmap/locale/hi/LC_MESSAGES/zenmap.mo	%{buildroot}/usr/share/zenmap/locale/hi/LC_MESSAGES/zenmap.mo
install -m 0755 /usr/share/zenmap/locale/hr/LC_MESSAGES/zenmap.mo	%{buildroot}/usr/share/zenmap/locale/hr/LC_MESSAGES/zenmap.mo
install -m 0755 /usr/share/zenmap/locale/it/LC_MESSAGES/zenmap.mo	%{buildroot}/usr/share/zenmap/locale/it/LC_MESSAGES/zenmap.mo
install -m 0755 /usr/share/zenmap/locale/ja/LC_MESSAGES/zenmap.mo	%{buildroot}/usr/share/zenmap/locale/ja/LC_MESSAGES/zenmap.mo
install -m 0755 /usr/share/zenmap/locale/pl/LC_MESSAGES/zenmap.mo	%{buildroot}/usr/share/zenmap/locale/pl/LC_MESSAGES/zenmap.mo
install -m 0755 /usr/share/zenmap/locale/pt_BR/LC_MESSAGES/zenmap.mo	%{buildroot}/usr/share/zenmap/locale/pt_BR/LC_MESSAGES/zenmap.mo
install -m 0755 /usr/share/zenmap/locale/ru/LC_MESSAGES/zenmap.mo	%{buildroot}/usr/share/zenmap/locale/ru/LC_MESSAGES/zenmap.mo
install -m 0755 /usr/share/zenmap/locale/zh/LC_MESSAGES/zenmap.mo	%{buildroot}/usr/share/zenmap/locale/zh/LC_MESSAGES/zenmap.mo
install -m 0755 /usr/share/zenmap/misc/profile_editor.xml	%{buildroot}/usr/share/zenmap/misc/profile_editor.xml
install -m 0755 /usr/share/zenmap/pixmaps/default_32.png	%{buildroot}/usr/share/zenmap/pixmaps/default_32.png
install -m 0755 /usr/share/zenmap/pixmaps/default_75.png	%{buildroot}/usr/share/zenmap/pixmaps/default_75.png
install -m 0755 /usr/share/zenmap/pixmaps/freebsd_32.png	%{buildroot}/usr/share/zenmap/pixmaps/freebsd_32.png
install -m 0755 /usr/share/zenmap/pixmaps/freebsd_75.png	%{buildroot}/usr/share/zenmap/pixmaps/freebsd_75.png
install -m 0755 /usr/share/zenmap/pixmaps/irix_32.png	%{buildroot}/usr/share/zenmap/pixmaps/irix_32.png
install -m 0755 /usr/share/zenmap/pixmaps/irix_75.png	%{buildroot}/usr/share/zenmap/pixmaps/irix_75.png
install -m 0755 /usr/share/zenmap/pixmaps/linux_32.png	%{buildroot}/usr/share/zenmap/pixmaps/linux_32.png
install -m 0755 /usr/share/zenmap/pixmaps/linux_75.png	%{buildroot}/usr/share/zenmap/pixmaps/linux_75.png
install -m 0755 /usr/share/zenmap/pixmaps/macosx_32.png	%{buildroot}/usr/share/zenmap/pixmaps/macosx_32.png
install -m 0755 /usr/share/zenmap/pixmaps/macosx_75.png	%{buildroot}/usr/share/zenmap/pixmaps/macosx_75.png
install -m 0755 /usr/share/zenmap/pixmaps/openbsd_32.png	%{buildroot}/usr/share/zenmap/pixmaps/openbsd_32.png
install -m 0755 /usr/share/zenmap/pixmaps/openbsd_75.png	%{buildroot}/usr/share/zenmap/pixmaps/openbsd_75.png
install -m 0755 /usr/share/zenmap/pixmaps/radialnet/border.png	%{buildroot}/usr/share/zenmap/pixmaps/radialnet/border.png
install -m 0755 /usr/share/zenmap/pixmaps/radialnet/firewall.png	%{buildroot}/usr/share/zenmap/pixmaps/radialnet/firewall.png
install -m 0755 /usr/share/zenmap/pixmaps/radialnet/logo.png	%{buildroot}/usr/share/zenmap/pixmaps/radialnet/logo.png
install -m 0755 /usr/share/zenmap/pixmaps/radialnet/padlock.png	%{buildroot}/usr/share/zenmap/pixmaps/radialnet/padlock.png
install -m 0755 /usr/share/zenmap/pixmaps/radialnet/router.png	%{buildroot}/usr/share/zenmap/pixmaps/radialnet/router.png
install -m 0755 /usr/share/zenmap/pixmaps/radialnet/switch.png	%{buildroot}/usr/share/zenmap/pixmaps/radialnet/switch.png
install -m 0755 /usr/share/zenmap/pixmaps/radialnet/wireless.png	%{buildroot}/usr/share/zenmap/pixmaps/radialnet/wireless.png
install -m 0755 /usr/share/zenmap/pixmaps/redhat_32.png	%{buildroot}/usr/share/zenmap/pixmaps/redhat_32.png
install -m 0755 /usr/share/zenmap/pixmaps/redhat_75.png	%{buildroot}/usr/share/zenmap/pixmaps/redhat_75.png
install -m 0755 /usr/share/zenmap/pixmaps/solaris_32.png	%{buildroot}/usr/share/zenmap/pixmaps/solaris_32.png
install -m 0755 /usr/share/zenmap/pixmaps/solaris_75.png	%{buildroot}/usr/share/zenmap/pixmaps/solaris_75.png
install -m 0755 /usr/share/zenmap/pixmaps/throbber.gif	%{buildroot}/usr/share/zenmap/pixmaps/throbber.gif
install -m 0755 /usr/share/zenmap/pixmaps/throbber.png	%{buildroot}/usr/share/zenmap/pixmaps/throbber.png
install -m 0755 /usr/share/zenmap/pixmaps/ubuntu_32.png	%{buildroot}/usr/share/zenmap/pixmaps/ubuntu_32.png
install -m 0755 /usr/share/zenmap/pixmaps/ubuntu_75.png	%{buildroot}/usr/share/zenmap/pixmaps/ubuntu_75.png
install -m 0755 /usr/share/zenmap/pixmaps/unknown_32.png	%{buildroot}/usr/share/zenmap/pixmaps/unknown_32.png
install -m 0755 /usr/share/zenmap/pixmaps/unknown_75.png	%{buildroot}/usr/share/zenmap/pixmaps/unknown_75.png
install -m 0755 /usr/share/zenmap/pixmaps/vl_1_32.png	%{buildroot}/usr/share/zenmap/pixmaps/vl_1_32.png
install -m 0755 /usr/share/zenmap/pixmaps/vl_1_75.png	%{buildroot}/usr/share/zenmap/pixmaps/vl_1_75.png
install -m 0755 /usr/share/zenmap/pixmaps/vl_2_32.png	%{buildroot}/usr/share/zenmap/pixmaps/vl_2_32.png
install -m 0755 /usr/share/zenmap/pixmaps/vl_2_75.png	%{buildroot}/usr/share/zenmap/pixmaps/vl_2_75.png
install -m 0755 /usr/share/zenmap/pixmaps/vl_3_32.png	%{buildroot}/usr/share/zenmap/pixmaps/vl_3_32.png
install -m 0755 /usr/share/zenmap/pixmaps/vl_3_75.png	%{buildroot}/usr/share/zenmap/pixmaps/vl_3_75.png
install -m 0755 /usr/share/zenmap/pixmaps/vl_4_32.png	%{buildroot}/usr/share/zenmap/pixmaps/vl_4_32.png
install -m 0755 /usr/share/zenmap/pixmaps/vl_4_75.png	%{buildroot}/usr/share/zenmap/pixmaps/vl_4_75.png
install -m 0755 /usr/share/zenmap/pixmaps/vl_5_32.png	%{buildroot}/usr/share/zenmap/pixmaps/vl_5_32.png
install -m 0755 /usr/share/zenmap/pixmaps/vl_5_75.png	%{buildroot}/usr/share/zenmap/pixmaps/vl_5_75.png
install -m 0755 /usr/share/zenmap/pixmaps/win_32.png	%{buildroot}/usr/share/zenmap/pixmaps/win_32.png
install -m 0755 /usr/share/zenmap/pixmaps/win_75.png	%{buildroot}/usr/share/zenmap/pixmaps/win_75.png
install -m 0755 /usr/share/zenmap/pixmaps/zenmap.png	%{buildroot}/usr/share/zenmap/pixmaps/zenmap.png
install -m 0755 /usr/share/zenmap/su-to-zenmap.sh	%{buildroot}/usr/share/zenmap/su-to-zenmap.sh
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
