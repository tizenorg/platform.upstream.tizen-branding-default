Name:           tizen-branding-default
Version:        0.1
Release:        1
License:        GPLv2+
Summary:        Default Branding files
Url:            http://tizen.org
Group:          System/Base
Source0:        %{name}-%{version}.tar.bz2
Source1001:     %{name}.manifest
BuildArch:      noarch
Requires:       plymouth-plugin-two-step
Requires(post): plymouth-scripts

%description
Default branding files.

%prep
%setup -q

%build
cp %{SOURCE1001} .


%install
mkdir -p %{buildroot}%{_datadir}/branding/default/syslinux
mkdir -p %{buildroot}%{_datadir}/plymouth/themes
cp syslinux/* %{buildroot}%{_datadir}/branding/default/syslinux
cp -a plymouth/tizen %{buildroot}%{_datadir}/plymouth/themes


%files
%manifest %{name}.manifest
%{_datadir}/branding/default/syslinux
%{_datadir}/plymouth/themes/tizen
