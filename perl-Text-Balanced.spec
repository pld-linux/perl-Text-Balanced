#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Balanced
Summary:	Text::Balanced - extract delimited text sequences from strings
Summary(pl):	Text::Balanced - wydzielanie z ³añcuchów rozgraniczonych ci±gów tekstowych
Name:		perl-Text-Balanced
Version:	1.89
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source:		http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Balanced Perl module - extract delimited text sequences from
strings.

%description -l pl
Modu³ Perla Text::Balanced - wydzielanie z ³añcuchów rozgraniczonych
ci±gów tekstowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Text/Balanced.pm
%{perl_sitearch}/auto/Text/Balanced
%{_mandir}/man3/*
