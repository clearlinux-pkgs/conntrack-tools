#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD55D978A8A1420E4 (coreteam@netfilter.org)
#
Name     : conntrack-tools
Version  : 1.4.7
Release  : 17
URL      : https://www.netfilter.org/projects/conntrack-tools/files/conntrack-tools-1.4.7.tar.bz2
Source0  : https://www.netfilter.org/projects/conntrack-tools/files/conntrack-tools-1.4.7.tar.bz2
Source1  : https://www.netfilter.org/projects/conntrack-tools/files/conntrack-tools-1.4.7.tar.bz2.sig
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
BuildRequires : pkgconfig(libtirpc)

%description
= Setting up active-active load-sharing hash-based stateful firewall =
by Pablo Neira Ayuso <pablo@netfilter.org> in 2010

%package bin
Summary: bin components for the conntrack-tools package.
Group: Binaries
Requires: conntrack-tools-license = %{version}-%{release}

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
%setup -q -n conntrack-tools-1.4.7
cd %{_builddir}/conntrack-tools-1.4.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1667013641
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1667013641
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/conntrack-tools
cp %{_builddir}/conntrack-tools-%{version}/COPYING %{buildroot}/usr/share/package-licenses/conntrack-tools/075d599585584bb0e4b526f5c40cb6b17e0da35a
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
/usr/lib64/conntrack-tools/ct_helper_slp.so
/usr/lib64/conntrack-tools/ct_helper_ssdp.so
/usr/lib64/conntrack-tools/ct_helper_tftp.so
/usr/lib64/conntrack-tools/ct_helper_tns.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/conntrack-tools/075d599585584bb0e4b526f5c40cb6b17e0da35a

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/conntrackd.conf.5
/usr/share/man/man8/conntrack.8
/usr/share/man/man8/conntrackd.8
/usr/share/man/man8/nfct.8
