#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Balanced
Summary:	Text::Balanced - extract delimited text sequences from strings
Summary(pl):	Text::Balanced - wydzielanie z ³añcuchów rozgraniczonych ci±gów tekstowych
Name:		perl-Text-Balanced
Version:	1.95
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:		http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1372379bb5cf036d8e8364ce9bfca27d
BuildRequires:	perl >= 5.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Text/Balanced.pm
%{_mandir}/man3/*
