%include	/usr/lib/rpm/macros.perl
Summary:	Text-Balanced perl module
Summary(pl):	Modu³ perla Text-Balanced
Name:		perl-Text-Balanced
Version:	1.52
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-Balanced-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Text-Balanced - extracts delimited text sequences from strings. 

%description -l pl
Text-Balanced - wydobywa okre¶lone sekwencje tekstu z ³añcuchów.

%prep
%setup -q -n Text-Balanced-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Text/Balanced
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Text/Balanced.pm
%{perl_sitearch}/auto/Text/Balanced

%{_mandir}/man3/*
