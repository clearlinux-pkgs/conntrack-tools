#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : conntrack-tools
Version  : 1.4.3
Release  : 7
URL      : http://www.netfilter.org/projects/conntrack-tools/files/conntrack-tools-1.4.3.tar.bz2
Source0  : http://www.netfilter.org/projects/conntrack-tools/files/conntrack-tools-1.4.3.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: conntrack-tools-bin
Requires: conntrack-tools-lib
Requires: conntrack-tools-doc
BuildRequires : bison
BuildRequires : flex
BuildRequires : pkgconfig(libmnl)
BuildRequires : pkgconfig(libnetfilter_conntrack)
BuildRequires : pkgconfig(libnetfilter_cthelper)
BuildRequires : pkgconfig(libnetfilter_cttimeout)
BuildRequires : pkgconfig(libnetfilter_queue)
BuildRequires : pkgconfig(libnfnetlink)

%description
This directory contains the files for the FT-FW based protocol

%package bin
Summary: bin components for the conntrack-tools package.
Group: Binaries

%description bin
bin components for the conntrack-tools package.


%package doc
Summary: doc components for the conntrack-tools package.
Group: Documentation

%description doc
doc components for the conntrack-tools package.


%package lib
Summary: lib components for the conntrack-tools package.
Group: Libraries

%description lib
lib components for the conntrack-tools package.


%prep
%setup -q -n conntrack-tools-1.4.3

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/conntrack
/usr/bin/conntrackd
/usr/bin/nfct

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/conntrack-tools/ct_helper_amanda.so
/usr/lib64/conntrack-tools/ct_helper_dhcpv6.so
/usr/lib64/conntrack-tools/ct_helper_ftp.so
/usr/lib64/conntrack-tools/ct_helper_rpc.so
/usr/lib64/conntrack-tools/ct_helper_sane.so
/usr/lib64/conntrack-tools/ct_helper_ssdp.so
/usr/lib64/conntrack-tools/ct_helper_tftp.so
/usr/lib64/conntrack-tools/ct_helper_tns.so
