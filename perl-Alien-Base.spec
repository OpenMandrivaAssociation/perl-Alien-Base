%define upstream_name    Alien-Base
%define upstream_version 0.042

%{?perl_default_filter}
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}^%{_docdir}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    API Reference for Alien:: Authors
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Alien/%{upstream_name}-%{upstream_version}.tar.gz

# for test purposes

BuildRequires: perl(Archive::Extract)
BuildRequires: perl(Capture::Tiny) >= 0.170.0
BuildRequires: perl(Cwd)
BuildRequires: perl-ExtUtils-MakeMaker
BuildRequires: perl(FFI::CheckLib) >= 0.110.0
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(File::chdir) >= 0.100.500
BuildRequires: perl(FindBin)
BuildRequires: perl(HTTP::Tiny) >= 0.44.0
BuildRequires: perl(JSON::PP)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Perl::OSType)
BuildRequires: perl(Shell::Config::Generate)
BuildRequires: perl(Shell::Guess)
BuildRequires: perl(Sort::Versions)
BuildRequires: perl(Test::More) >= 0.940.0
#BuildRequires: perl(Test2::Bundle::Extended)
BuildRequires: perl(Text::ParseWords) >= 3.260.0
BuildRequires: perl(URI)
BuildRequires: perl(parent)
BuildRequires: pkgconfig(zlib)
BuildArch:  noarch

%description
the Alien::Base manpage comprises base classes to help in the construction
of 'Alien::' modules. Modules in the the Alien manpage namespace are used
to locate and install (if necessary) external libraries needed by other
Perl modules.

This is the documentation for the the Alien::Base manpage module itself. To
learn more about the system as a whole please see the
Alien::Base::Authoring manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc Changes LICENSE MYMETA.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*
