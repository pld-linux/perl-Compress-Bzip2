%include	/usr/lib/rpm/macros.perl
Summary:	Compress-Bzip2 perl module
Summary(pl):	Modu³ perla Compress-Bzip2
Name:		perl-Compress-Bzip2
Version:	1.00
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Compress/Compress-Bzip2-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	bzip2-devel >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compress-Bzip2 - Interface to Bzip2 compression library.

%description -l pl
Compress-Bzip2 - interfejs do biblioteki Bzip2.

%prep
%setup -q -n Compress-Bzip2-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Compress/Bzip2.pm
%dir %{perl_sitearch}/auto/Compress/Bzip2
%{perl_sitearch}/auto/Compress/Bzip2/Bzip2.bs
%{perl_sitearch}/auto/Compress/Bzip2/autosplit.ix
%attr(755,root,root) %{perl_sitearch}/auto/Compress/Bzip2/Bzip2.so
%{_mandir}/man3/*
