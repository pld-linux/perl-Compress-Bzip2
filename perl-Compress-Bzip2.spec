#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Compress
%define		pnam	Bzip2
Summary:	Compress::Bzip2 - Perl interface to Bzip2 compression library
Summary(pl.UTF-8):	Compress::Bzip2 - interfejs perlowy do biblioteki kompresji Bzip2
Name:		perl-Compress-Bzip2
Version:	2.26
Release:	8
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Compress/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	062aa57d7b83e7eec05cf37dcea643e6
URL:		http://search.cpan.org/dist/Compress-Bzip2/
BuildRequires:	bzip2-devel >= 1.0.0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Compress::Bzip2 module provides a Perl interface to the Bzip2
compression library. A relevant subset of the functionality provided
by Bzip2 is available in Compress::Bzip2.

%description -l pl.UTF-8
Moduł Compress::Bzip2 udostępnia interfejs perlowy do biblioteki
kompresji Bzip2. Compress::Bzip2 udostępnia związany z tym podzbiór
zbioru funkcji udostępnianych przez Bzip2.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%doc README.md NEWS
%{perl_vendorarch}/Compress/Bzip2.pm
%dir %{perl_vendorarch}/auto/Compress/Bzip2
%{perl_vendorarch}/auto/Compress/Bzip2/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Compress/Bzip2/Bzip2.so
%{_mandir}/man3/*
