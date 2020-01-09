### Name: ElRepo.org Community Enterprise Linux Repository for el6
### URL: http://elrepo.org/

Summary: ElRepo.org Community Enterprise Linux Repository release file
Name: elrepo-release
Version: 6
Release: 2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://elrepo.org/

Source0: elrepo.repo
Source1: RPM-GPG-KEY-elrepo.org

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-build-%(%{__id_u} -n)
BuildArch: noarch

%description
This package contains yum configuration for the ElRepo.org Community Enterprise Linux Repository, as well as the public GPG keys used to sign packages.

%prep
%setup -c -T

%build
# Nothing to build

%install
%{__rm} -rf %{buildroot}
%{__cp} -a %{SOURCE1} .
%{__install} -Dpm 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/elrepo.repo
%{__install} -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-elrepo.org

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%pubkey RPM-GPG-KEY-elrepo.org
%dir %{_sysconfdir}/yum.repos.d/
%config(noreplace) %{_sysconfdir}/yum.repos.d/elrepo.repo
%dir %{_sysconfdir}/pki/rpm-gpg/
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-elrepo.org

%changelog
* Mon Nov 15 2010 Akemi Yagi <toracat@elrepo.org> - 6-2
- Incorrect tag corrected.

* Thu Nov 11 2010 Akemi Yagi <toracat@elrepo.org> - 6-1
- First 6.x version 

* Thu Oct 21 2010 Akemi Yagi <toracat@elrepo.org> - 5-1
- Release number now has 5-x format
- Added kernel repo
- Removed fasttrack repo
- Added mirror sites

* Sat Mar 14 2009 Philip J Perry <phil@elrepo.org> - 0.1-1
- Initial elrepo-release package.
