Name:		alsa-topology-conf
Summary:	Topology configuration for ALSA
Version:	1.2.5.1
Release:	2
License:	BSD 3-clause
Source0:	https://www.alsa-project.org/files/pub/lib/alsa-topology-conf-%{version}.tar.bz2
BuildArch:	noarch

%description
Topology configuration for ALSA

%prep
%autosetup -p1

%build

%install
mkdir -p %{buildroot}%{_datadir}/alsa
cp -a topology %{buildroot}%{_datadir}/alsa/

%files
%{_datadir}/alsa/topology
