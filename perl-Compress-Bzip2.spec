#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Compress
%define	pnam	Bzip2
Summary:	Compress::Bzip2 - Perl interface to Bzip2 compression library
Summary(pl):	Compress::Bzip2 - interfejs perlowy do biblioteki kompresji Bzip2
Name:		perl-Compress-Bzip2
Version:	1.02
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:	http://www.cpan.org/modules/by-authors/id/K/KC/KCARNUT/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3ff9ac323a45fe8484fdc9f0313c5f3f
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	bzip2-devel >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Compress::Bzip2 module provides a Perl interface to the Bzip2
compression library. A relevant subset of the functionality provided
by Bzip2 is available in Compress::Bzip2.

%description -l pl
Moduł Compress::Bzip2 udostępnia interfejs perlowy do biblioteki
kompresji Bzip2. Compress::Bzip2 udostępnia związany z tym podzbiór
zbioru funkcji udostępnianych przez Bzip2.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"
%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%{perl_vendorarch}/Compress/Bzip2.pm
%dir %{perl_vendorarch}/auto/Compress/Bzip2
%{perl_vendorarch}/auto/Compress/Bzip2/Bzip2.bs
%{perl_vendorarch}/auto/Compress/Bzip2/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Compress/Bzip2/Bzip2.so
%{_mandir}/man3/*
