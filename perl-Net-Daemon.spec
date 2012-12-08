%define upstream_name 	 Net-Daemon
%define upstream_version 0.48

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl extension for portable daemons
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/J/JW/JWIED/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Net::Daemon is an abstract base class for implementing portable server
applications in a very simple way. The module is designed for Perl 5.005 and
threads, but can work with fork() and Perl 5.004.

The Net::Daemon class offers methods for the most common tasks a daemon needs:
Starting up, logging, accepting clients, authorization, restricting its own
environment for security and doing the true work. You only have to override
those methods that aren't appropriate for you, but typically inheriting will
safe you a lot of work anyways.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# don't work on the cluster
# %{__make} test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Net
%{_mandir}/*/*

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.480.0-4mdv2012.0
+ Revision: 765522
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.480.0-3
+ Revision: 764038
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.480.0-2
+ Revision: 667272
- mass rebuild

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.480.0-1
+ Revision: 643413
- update to new version 0.48

* Tue Mar 01 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.460.0-1
+ Revision: 641148
- update to 0.46

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.430.0-1mdv2011.0
+ Revision: 404070
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.43-3mdv2009.0
+ Revision: 223849
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.43-2mdv2008.1
+ Revision: 180502
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Jul 07 2007 Funda Wang <fwang@mandriva.org> 0.43-1mdv2008.0
+ Revision: 49329
- Corrected tarball dirname
- New version

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.39-2mdv2008.0
+ Revision: 23468
- disable test because iurt
- rebuild


* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.39-1mdk
- new version
- rpmbuildupdate aware
- spec cleanup
- %%mkrel
- enable tests
- better summary and description

* Mon Jun 06 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.38-2mdk
- Rebuild

* Wed Apr 21 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.38-1mdk
- 0.38

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.37-3mdk
- rebuild for new perl
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

* Fri May 16 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.37-2mdk
- rebuild for dependencies

* Fri Apr 25 2003 François Pons <fpons@mandrakesoft.com> 0.37-1mdk
- 0.37.

