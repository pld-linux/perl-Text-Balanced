#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Balanced
Summary:	Text-Balanced perl module
Summary(pl):	Modu³ perla Text-Balanced
Name:		perl-Text-Balanced
Version:	1.90
Release:	1
Copyright:	GPL
Group:		Development/Languages/Perl
Source:		http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-Balanced - extracts delimited text sequences from strings. 

%description -l pl
Text-Balanced - wydobywa okre¶lone sekwencje tekstu z ³añcuchów.

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
