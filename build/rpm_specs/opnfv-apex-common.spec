%global srcname opnfv-apex

Name:		python34-%{srcname}
Version:	5.0
Release:	%{_release}
Summary:	Scripts for OPNFV deployment using Apex

Group:		System Environment
License:	Apache 2.0
URL:		https://gerrit.opnfv.org/gerrit/apex.git
Source0:	opnfv-apex-common.tar.gz

BuildArch:      noarch
BuildRequires:  python-docutils python34-devel
Requires:       opnfv-apex-sdn opnfv-apex-undercloud openvswitch qemu-kvm bridge-utils libguestfs-tools python34-libvirt
Requires:       initscripts net-tools iputils iproute iptables python34 python34-yaml python34-jinja2 python3-ipmi python34-virtualbmc
Requires:       ipxe-roms-qemu >= 20160127-1
Requires:       libvirt-devel ansible
Requires:       python34-iptables python34-cryptography python34-pbr

%description
Scripts for OPNFV deployment using Apex
https://wiki.opnfv.org/apex

%prep
%autosetup -n %{srcname}-%{version}

%build
rst2html docs/release/installation/index.rst docs/release/installation/installation-instructions.html
rst2html docs/release/release-notes/release-notes.rst docs/release/release-notes/release-notes.html
%py3_build

%global __python %{__python3}

%install
mkdir -p %{buildroot}%{_bindir}/
%py3_install
install ci/util.sh %{buildroot}%{_bindir}/opnfv-util

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
install build/bash_completion_apex %{buildroot}%{_sysconfdir}/bash_completion.d/apex

mkdir -p %{buildroot}%{_sysconfdir}/opnfv-apex/
cp -f %{buildroot}%{_datadir}/opnfv-apex/config/deploy/* %{buildroot}%{_sysconfdir}/opnfv-apex/
cp -f %{buildroot}%{_datadir}/opnfv-apex/config/network/* %{buildroot}%{_sysconfdir}/opnfv-apex/
rm -f %{buildroot}%{_sysconfdir}/opnfv-apex/os-odl-csit-noha.yaml
rm -f %{buildroot}%{_sysconfdir}/opnfv-apex/deploy_settings.yaml

mkdir -p %{buildroot}%{_docdir}/opnfv/
install LICENSE.rst %{buildroot}%{_docdir}/opnfv/
install docs/release/installation/installation-instructions.html %{buildroot}%{_docdir}/opnfv/
install docs/release/release-notes/index.rst %{buildroot}%{_docdir}/opnfv/release-notes.rst
install docs/release/release-notes/release-notes.html %{buildroot}%{_docdir}/opnfv/
install config/deploy/deploy_settings.yaml %{buildroot}%{_docdir}/opnfv/deploy_settings.yaml.example
install config/network/network_settings.yaml %{buildroot}%{_docdir}/opnfv/network_settings.yaml.example
install config/network/network_settings_v6.yaml %{buildroot}%{_docdir}/opnfv/network_settings_v6.yaml.example
install config/network/network_settings_vpp.yaml %{buildroot}%{_docdir}/opnfv/network_settings_vpp.yaml.example
install config/inventory/pod_example_settings.yaml %{buildroot}%{_docdir}/opnfv/inventory.yaml.example

%files
%{python3_sitelib}/apex/
%{python3_sitelib}/apex-*.egg-info
%defattr(644, root, root, 644)
%attr(755,root,root) %{_bindir}/opnfv-deploy
%attr(755,root,root) %{_bindir}/opnfv-clean
%attr(755,root,root) %{_bindir}/opnfv-util
%{_datadir}/opnfv-apex/
%{_sysconfdir}/bash_completion.d/apex
%{_sysconfdir}/opnfv-apex/os-nosdn-nofeature-noha.yaml
%{_sysconfdir}/opnfv-apex/os-nosdn-bar-noha.yaml
%{_sysconfdir}/opnfv-apex/os-nosdn-bar-ha.yaml
%{_sysconfdir}/opnfv-apex/os-nosdn-calipso-noha.yaml
%{_sysconfdir}/opnfv-apex/os-nosdn-fdio-noha.yaml
%{_sysconfdir}/opnfv-apex/os-nosdn-fdio-ha.yaml
%{_sysconfdir}/opnfv-apex/os-nosdn-ovs_dpdk-noha.yaml
%{_sysconfdir}/opnfv-apex/os-nosdn-nofeature-ha.yaml
%{_sysconfdir}/opnfv-apex/os-nosdn-performance-ha.yaml
%{_sysconfdir}/opnfv-apex/os-nosdn-ovs_dpdk-ha.yaml
%{_sysconfdir}/opnfv-apex/os-nosdn-kvm-ha.yaml
%{_sysconfdir}/opnfv-apex/os-nosdn-kvm-noha.yaml
%{_sysconfdir}/opnfv-apex/os-nosdn-kvm_ovs_dpdk-ha.yaml
%{_sysconfdir}/opnfv-apex/os-nosdn-kvm_ovs_dpdk-noha.yaml
%{_sysconfdir}/opnfv-apex/os-odl-bgpvpn-ha.yaml
%{_sysconfdir}/opnfv-apex/os-odl-bgpvpn-noha.yaml
%{_sysconfdir}/opnfv-apex/os-odl-sfc-ha.yaml
%{_sysconfdir}/opnfv-apex/os-odl-sfc-noha.yaml
%{_sysconfdir}/opnfv-apex/os-odl-fdio-noha.yaml
%{_sysconfdir}/opnfv-apex/os-odl_netvirt-fdio-noha.yaml
%{_sysconfdir}/opnfv-apex/os-odl-fdio-ha.yaml
%{_sysconfdir}/opnfv-apex/os-odl-fdio_dvr-ha.yaml
%{_sysconfdir}/opnfv-apex/os-odl-fdio_dvr-noha.yaml
%{_sysconfdir}/opnfv-apex/os-odl-ovs_dpdk-noha.yaml
%{_sysconfdir}/opnfv-apex/os-odl-ovs_dpdk-ha.yaml
%{_sysconfdir}/opnfv-apex/os-odl-nofeature-ha.yaml
%{_sysconfdir}/opnfv-apex/os-odl-nofeature-noha.yaml
%{_sysconfdir}/opnfv-apex/os-odl-gluon-noha.yaml
%{_sysconfdir}/opnfv-apex/os-ovn-nofeature-noha.yaml
%{_sysconfdir}/opnfv-apex/os-onos-nofeature-ha.yaml
%{_sysconfdir}/opnfv-apex/os-onos-sfc-ha.yaml
%{_sysconfdir}/opnfv-apex/os-ocl-nofeature-ha.yaml
%{_sysconfdir}/opnfv-apex/network_settings.yaml
%{_sysconfdir}/opnfv-apex/network_settings_vlans.yaml
%{_sysconfdir}/opnfv-apex/network_settings_v6.yaml
%{_sysconfdir}/opnfv-apex/network_settings_vpp.yaml
%doc %{_docdir}/opnfv/LICENSE.rst
%doc %{_docdir}/opnfv/installation-instructions.html
%doc %{_docdir}/opnfv/release-notes.rst
%doc %{_docdir}/opnfv/release-notes.html
%doc %{_docdir}/opnfv/deploy_settings.yaml.example
%doc %{_docdir}/opnfv/network_settings.yaml.example
%doc %{_docdir}/opnfv/network_settings_v6.yaml.example
%doc %{_docdir}/opnfv/network_settings_vpp.yaml.example
%doc %{_docdir}/opnfv/inventory.yaml.example

%changelog
* Wed Sep 20 2017 Tim Rozet <trozet@redhat.com> - 5.0-7
- Add calipso
* Fri Sep 08 2017 Tim Rozet <trozet@redhat.com> - 5.0-6
- Updates clean to use python
* Wed Aug 23 2017 Tim Rozet <trozet@redhat.com> - 5.0-5
- Updated requirements
* Mon Aug 14 2017 Tim Rozet <trozet@redhat.com> - 5.0-4
- Updated for python refactoring
* Mon May 08 2017 Dan Radez <dradez@redhat.com> - 5.0-3
- adding configure-vm
* Tue Apr 11 2017 Dan Radez <dradez@redhat.com> - 5.0-2
- Remove l2 scenario files
* Tue Apr 04 2017 Dan Radez <dradez@redhat.com> - 5.0-1
- Version update for Euphrates
- rename to ovs_dpdk
* Wed Mar 29 2017 Dan Radez <dradez@redhat.com> - 4.0-9
- Remove odl_l2-nofeature scenario file
- rename all odl_l3 scenario files to odl
* Thu Mar 23 2017 Tim Rozet <trozet@redhat.com> - 4.0-8
- Adds os-odl_l3-ovs-ha and noha scenarios
* Sun Mar 12 2017 Feng Pan <fpan@redhat.com> - 4.0-7
- Add os-nosdn-fdio-ha.yaml
* Fri Mar 10 2017 Feng Pan <fpan@redhat.com> - 4.0-6
- Add os-odl_l3-fdio-noha.yaml and os-odl_l3-fdio-ha.yaml
* Wed Mar 08 2017 Dan Radez <dradez@redhat.com> - 4.0-5
- Adding kvm4nfv files
- Adding OVN files
* Tue Feb 14 2017 Feng Pan <fpan@redhat.com> - 4.0-4
- Add network_settings_vpp.yaml
* Fri Feb 3 2017 Nikolas Hermanns <nikolas.hermanns@ericsson.com> - 4.0-3
- change odl_l3-gluon-noha to odl-gluon-noha
* Thu Feb 2 2017 Feng Pan <fpan@redhat.com> - 4.0-2
- Add odl_l3-gluon-noha config file
* Wed Nov 2 2016 Dan Radez <dradez@redhat.com> - 4.0-1
- Version update for Danube
* Fri Sep 16 2016 Dan Radez <dradez@redhat.com> - 3.0-13
- adding bash completion script
* Tue Aug 30 2016 Tim Rozet <trozet@redhat.com> - 3.0-12
- Add clean library.
* Mon Aug 1 2016 Tim Rozet <trozet@redhat.com> - 3.0-11
- Add nosdn fdio scenarios.
* Tue Jul 5 2016 Dan Radez <dradez@redhat.com> - 3.0-10
- Adding functions.sh files
* Wed Jun 15 2016 Tim Rozet <trozet@redhat.com> - 3.0-9
- Add fdio scenarios.
* Tue Jun 14 2016 Feng Pan <fpan@redhat.com> - 3.0-8
- Add network_settings_v6.yaml
* Thu Jun 2 2016 Michael Chapman <michapma@redhat.com> - 3.0-7
- Add custom libvirt domain.xml.
* Wed Jun 1 2016 Feng Pan <fpan@redhat.com> - 3.0-6
- Add performance deployment file
* Sun May 15 2016 Feng Pan <fpan@redhat.com> - 3.0-5
- Fixes python3 dependency.
* Sun May 8 2016 Feng Pan <fpan@redhat.com> - 3.0-4
- Adds dependency for python34-setuptools
* Fri Apr 22 2016 Feng Pan <fpan@redhat.com> - 3.0-3
- Adds python network setting parsing lib.
* Fri Apr 15 2016 Feng Pan <fpan@redhat.com> - 3.0-2
- Adds python ip utility lib.
* Mon Apr 11 2016 Tim Rozet <trozet@redhat.com> - 3.0-1
- adding opnfv-util
* Mon Apr 04 2016 Dan Radez <dradez@redhat.com> - 3.0-0
- Version update for Colorado
* Mon Apr 04 2016 Dan Radez <dradez@redhat.com> - 2.2-0
- adding dependencies initscripts net-tools iputils iproute iptables
* Wed Jan 27 2016 Tim Rozet <trozet@redhat.com> - 2.1-4
- Adds example inventory file and nosdn scenario
* Wed Jan 20 2016 Dan Radez <dradez@redhat.com> - 2.1-3
- Updating the installation instructions
* Thu Jan 14 2016 Dan Radez <dradez@redhat.com> - 2.1-2
- Package Split
