%define modname	Net-Daemon
%define modver	0.48

Summary:	Perl extension for portable daemons
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	12
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/J/JW/JWIED/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# don't work on the cluster
#make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Net
%{_mandir}/man3/*

