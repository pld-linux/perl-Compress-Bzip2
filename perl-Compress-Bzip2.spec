%include	/usr/lib/rpm/macros.perl
%define		pdir	Compress
%define		pnam	Bzip2
Summary:	Compress::Bzip2 perl module
Summary(pl):	Modu� perla Compress::Bzip2
Name:		perl-Compress-Bzip2
Version:	1.00
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	bzip2-devel >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compress::Bzip2 - Interface to Bzip2 compression library.

%description -l pl
Compress::Bzip2 - interfejs do biblioteki Bzip2.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%{perl_sitearch}/Compress/Bzip2.pm
%dir %{perl_sitearch}/auto/Compress/Bzip2
%{perl_sitearch}/auto/Compress/Bzip2/Bzip2.bs
%{perl_sitearch}/auto/Compress/Bzip2/autosplit.ix
%attr(755,root,root) %{perl_sitearch}/auto/Compress/Bzip2/Bzip2.so
%{_mandir}/man3/*
