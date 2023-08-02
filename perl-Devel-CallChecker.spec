#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Devel-CallChecker
Version  : 0.009
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Devel-CallChecker-0.009.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Devel-CallChecker-0.009.tar.gz
Summary  : 'custom op checking attached to subroutines'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Devel-CallChecker-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(DynaLoader::Functions)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Devel::CallChecker - custom op checking attached to subroutines
DESCRIPTION

%package dev
Summary: dev components for the perl-Devel-CallChecker package.
Group: Development
Provides: perl-Devel-CallChecker-devel = %{version}-%{release}
Requires: perl-Devel-CallChecker = %{version}-%{release}

%description dev
dev components for the perl-Devel-CallChecker package.


%package perl
Summary: perl components for the perl-Devel-CallChecker package.
Group: Default
Requires: perl-Devel-CallChecker = %{version}-%{release}

%description perl
perl components for the perl-Devel-CallChecker package.


%prep
%setup -q -n Devel-CallChecker-0.009
cd %{_builddir}/Devel-CallChecker-0.009

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::CallChecker.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
