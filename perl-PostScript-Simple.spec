%define upstream_name	 PostScript-Simple
%define upstream_version 0.09
Name:		perl-%{upstream_name}
Version:	0.09
Release:	1

Summary:	Produce PostScript files from Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/PostScript-Simple
Source0:	https://cpan.metacpan.org/authors/id/M/MC/MCNEWTON/PostScript-Simple-0.09.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
The PostScript::Simple module allows you to have a simple method of writing
PostScript files from Perl. It has graphics primitives that allow lines,
curves, circles, polygons and boxes to be drawn. Text can be added to the page
using standard PostScript fonts.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README TODO
%{perl_vendorlib}/PostScript/*
%{_mandir}/*/*


