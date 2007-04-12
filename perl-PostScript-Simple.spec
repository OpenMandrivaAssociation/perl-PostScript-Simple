%define module	PostScript-Simple
%define name	perl-%{module}
%define version	0.07
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Produce PostScript files from Perl
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel

%description
The PostScript::Simple module allows you to have a simple method of writing
PostScript files from Perl. It has graphics primitives that allow lines,
curves, circles, polygons and boxes to be drawn. Text can be added to the page
using standard PostScript fonts.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README TODO
%{perl_vendorlib}/PostScript/*
%{_mandir}/*/*

