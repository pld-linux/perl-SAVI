%include	/usr/lib/rpm/macros.perl
Summary:	Perl module interface to the Sophos Anti-Virus engine
Summary(pl):	Modu³ Perla bêd±cy interfejsem do silnika Sophos Anti-Virus
Name:		perl-SAVI
Version:	0.15
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.csupomona.edu/~henson/www/projects/SAVI-Perl/dist/SAVI-Perl-%{version}.tar.gz
BuildRequires:	perl >= 5.005
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libsavi.so.2

%description
SAVI-Perl is a Perl module interface to the Sophos Anti-Virus engine.
It allows you to scan files for viruses directly from Perl.

%description -l pl
SAVI-Perl to modu³ Perla bêd±cy interfejsem do silnika Sophos
Anti-Virus. Pozwala na przeszukiwanie plików pod k±tem wirusów
bezpo¶rednio z Perla.

%prep
%setup -q -n SAVI-Perl-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README example/*
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/SAVI
%{perl_vendorarch}/auto/SAVI/*.bs
%attr(755, root, root) %{perl_vendorarch}/auto/SAVI/*.so
%{_mandir}/man3/*
