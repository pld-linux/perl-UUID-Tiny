#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	UUID
%define		pnam	Tiny
Summary:	UUID::Tiny - Pure Perl UUID Support With Functional Interface
Summary(pl.UTF-8):	UUID::Tiny - czysto perlowa obsługa UUID-ów z interfejsem funkcyjnym
Name:		perl-UUID-Tiny
Version:	1.04
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/UUID/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2d7c18711e64e0a64cc7c7fbb870947e
URL:		https://metacpan.org/release/UUID-Tiny
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Time-HiRes
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UUID::Tiny is a lightweight, low dependency Pure Perl module for UUID
creation and testing. This module provides the creation of version 1
time based UUIDs (using random multicast MAC addresses), version 3 MD5
based UUIDs, version 4 random UUIDs, and version 5 SHA-1 based UUIDs.

%description -l pl.UTF-8
UUID::Tiny to lekki, mający mało zależności, napisany w czystym Perlu
moduł do tworzenia i testowania UUID-ów. Udostępnia tworzenie UUID-ów
w wersji 1 opartych na czasie (wykorzystujących losowe adresy
multicastowe MAC), UUID-ów w wersji 3 opartych na MD5, UUID-ów
losowych w wersji 4 oraz UUID-ów w wersji 5 opartych na SHA-1.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/UUID/Tiny.pm
%{_mandir}/man3/UUID::Tiny.3pm*
