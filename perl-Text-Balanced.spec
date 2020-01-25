#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Text
%define		pnam	Balanced
Summary:	Text::Balanced - extract delimited text sequences from strings
Summary(pl.UTF-8):	Text::Balanced - wydzielanie z łańcuchów rozgraniczonych ciągów tekstowych
Name:		perl-Text-Balanced
Version:	2.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	891fa8a0f20307a5f22ac1fdd0ce565b
URL:		http://search.cpan.org/dist/Text-Balanced/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Balanced Perl module - extract delimited text sequences from
strings.

%description -l pl.UTF-8
Moduł Perla Text::Balanced - wydzielanie z łańcuchów rozgraniczonych
ciągów tekstowych.

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
