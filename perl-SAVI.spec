#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	SAVI
Summary:	SAVI - Perl interface to the Sophos Anti-Virus engine
Summary(pl.UTF-8):	SAVI - interfejs perlowy do silnika antywirusa Sophos
Name:		perl-SAVI
Version:	0.25
Release:	1
License:	GPL v1+
Group:		Development/Languages/Perl
Source0:	http://www.csupomona.edu/~henson/www/projects/SAVI-Perl/dist/SAVI-Perl-%{version}.tar.gz
# Source0-md5:	f53c5764e668e5d6c59e4713f8ee83b5
URL:		http://search.cpan.org/dist/SAVI-/
BuildRequires:	A-FUCKING-BRAIN-AND-PROPRIETARY-LIB!
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libsavi.so.2

%description
SAVI-Perl is a Perl module interface to the Sophos Anti-Virus engine.
It allows you to scan files for viruses directly from Perl.

%description -l pl.UTF-8
SAVI-Perl to moduł Perla będący interfejsem do silnika Sophos
Anti-Virus. Pozwala na przeszukiwanie plików pod kątem wirusów
bezpośrednio z Perla.

%prep
%setup -q -n SAVI-Perl-%{version}

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
%doc README example/*
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/SAVI
%attr(755, root, root) %{perl_vendorarch}/auto/SAVI/*.so
%{_mandir}/man3/*
