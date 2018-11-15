#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xAB4655A126D292E4 (coreteam@netfilter.org)
#
Name     : conntrack-tools
Version  : 1.4.5
Release  : 13
URL      : http://www.netfilter.org/projects/conntrack-tools/files/conntrack-tools-1.4.5.tar.bz2
Source0  : http://www.netfilter.org/projects/conntrack-tools/files/conntrack-tools-1.4.5.tar.bz2
Source99 : http://www.netfilter.org/projects/conntrack-tools/files/conntrack-tools-1.4.5.tar.bz2.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: conntrack-tools-bin = %{version}-%{release}
Requires: conntrack-tools-lib = %{version}-%{release}
Requires: conntrack-tools-license = %{version}-%{release}
Requires: conntrack-tools-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : flex
BuildRequires : pkgconfig(libmnl)
BuildRequires : pkgconfig(libnetfilter_conntrack)
BuildRequires : pkgconfig(libnetfilter_cthelper)
BuildRequires : pkgconfig(libnetfilter_cttimeout)
BuildRequires : pkgconfig(libnetfilter_queue)
BuildRequires : pkgconfig(libnfnetlink)
BuildRequires : pkgconfig(libsystemd)

%description
This directory contains the files for the FT-FW based protocol

%package bin
Summary: bin components for the conntrack-tools package.
Group: Binaries
Requires: conntrack-tools-license = %{version}-%{release}
Requires: conntrack-tools-man = %{version}-%{release}

%description bin
bin components for the conntrack-tools package.


%package lib
Summary: lib components for the conntrack-tools package.
Group: Libraries
Requires: conntrack-tools-license = %{version}-%{release}

%description lib
lib components for the conntrack-tools package.


%package license
Summary: license components for the conntrack-tools package.
Group: Default

%description license
license components for the conntrack-tools package.


%package man
Summary: man components for the conntrack-tools package.
Group: Default

%description man
man components for the conntrack-tools package.


%prep
%setup -q -n conntrack-tools-1.4.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542310100
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1542310100
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/conntrack-tools
cp COPYING %{buildroot}/usr/share/package-licenses/conntrack-tools/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/conntrack
/usr/bin/conntrackd
/usr/bin/nfct

%files lib
%defattr(-,root,root,-)
/usr/lib64/conntrack-tools/ct_helper_amanda.so
/usr/lib64/conntrack-tools/ct_helper_dhcpv6.so
/usr/lib64/conntrack-tools/ct_helper_ftp.so
/usr/lib64/conntrack-tools/ct_helper_mdns.so
/usr/lib64/conntrack-tools/ct_helper_rpc.so
/usr/lib64/conntrack-tools/ct_helper_sane.so
/usr/lib64/conntrack-tools/ct_helper_ssdp.so
/usr/lib64/conntrack-tools/ct_helper_tftp.so
/usr/lib64/conntrack-tools/ct_helper_tns.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/conntrack-tools/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/conntrackd.conf.5
/usr/share/man/man8/conntrack.8
/usr/share/man/man8/conntrackd.8
/usr/share/man/man8/nfct.8
