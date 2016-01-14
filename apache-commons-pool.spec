%global pkg_name apache-commons-pool
%{?scl:%scl_package %{pkg_name}}
%{?java_common_find_provides_and_requires}

%global base_name       pool
%global short_name      commons-%{base_name}

Name:             %{?scl_prefix}%{pkg_name}
Version:          1.6
Release:          9.12%{?dist}
Summary:          Apache Commons Pool Package
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:        noarch

BuildRequires:    %{?scl_prefix}javapackages-tools
BuildRequires:    %{?scl_prefix}maven-local
BuildRequires:    %{?scl_prefix_maven}apache-commons-parent >= 26-7

%description
The goal of Pool package is it to create and maintain an object (instance)
pooling package to be distributed under the ASF license. The package should
support a variety of pool implementations, but encourage support of an
interface that makes these implementations interchangeable.

%package javadoc
Summary:          Javadoc for %{pkg_name}
# This should go away with F-17

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -n %{short_name}-%{version}-src
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_file : %{pkg_name} %{short_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc README.txt LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.6-9.12
- Mass rebuild 2015-01-13

* Fri Jan 09 2015 Michal Srb <msrb@redhat.com> - 1.6-9.11
- Mass rebuild 2015-01-09

* Tue Dec 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-9.10
- Migrate requires and build-requires to rh-java-common

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-9.9
- Mass rebuild 2014-12-15

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-9.8
- Rebuild for rh-java-common collection

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-9.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-9.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-9.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-9.4
- Remove requires on java

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-9.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-9.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-9.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.6-9
- Mass rebuild 2013-12-27

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-8
- Add BuildRequires on apache-commons-parent >= 26-7

* Thu Aug 15 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.6-7
- Migrate away from mvn-rpmbuild (#997428)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Tue Feb 19 2013 Mat Booth <fedora@matbooth.co.uk> - 1.6-5
- Add missing BuildRequires maven-local

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-3
- Install NOTICE file with javadoc package

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 13 2012 Alexander Kurtakov <akurtako@redhat.com> 1.6-1
- Update to latest release - 1.6.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Alexander Kurtakov <akurtako@redhat.com> 1.5.7-1
- Update to latest version (1.5.7).

* Wed Nov 30 2011 Alexander Kurtakov <akurtako@redhat.com> 1.5.6-2
- Adapt to current guidelines.

* Fri Apr 15 2011 Chris Spike <spike@fedoraproject.org> 1.5.6-1
- Updated to 1.5.6
- Fixed build for maven 3

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 9 2010 Chris Spike <spike@fedoraproject.org> 1.5.5-4
- Removed maven* BRs in favour of apache-commons-parent
- Added deprecated groupId to depmap for compatibility reasons

* Mon Oct 18 2010 Chris Spike <spike@fedoraproject.org> 1.5.5-3
- Removed Epoch

* Tue Oct 5 2010 Chris Spike <spike@fedoraproject.org> 1.5.5-2
- Consistently using 'buildroot' macro instead of 'RPM_BUILD_ROOT' now

* Fri Oct 1 2010 Chris Spike <spike@fedoraproject.org> 1.5.5-1
- Rename and rebase from jakarta-commons-pool
