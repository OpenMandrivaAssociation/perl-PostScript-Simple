%define upstream_name	 PostScript-Simple
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Produce PostScript files from Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The PostScript::Simple module allows you to have a simple method of writing
PostScript files from Perl. It has graphics primitives that allow lines,
curves, circles, polygons and boxes to be drawn. Text can be added to the page
using standard PostScript fonts.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 408032
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.07-4mdv2009.0
+ Revision: 241845
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.07-2mdv2008.0
+ Revision: 25106
- rebuild


* Wed Mar 22 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.07-1mdk
- 0.07

* Thu Jan 06 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.06-1mdk
- Initial MDK release.

