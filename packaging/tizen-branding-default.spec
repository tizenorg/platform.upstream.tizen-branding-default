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
Recommends:     plymouth-plugin-two-step
Requires(pre):  glib2-tools
Requires(postun): glib2-tools

%description
Default branding files.

%prep
%setup -q

%build
cp %{SOURCE1001} .


%install
mkdir -p %{buildroot}%{_datadir}/branding/default/syslinux
mkdir -p %{buildroot}%{_datadir}/branding/default/backgrounds
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas

cp backgrounds/Blue_Dock_by_dimage.jpg %{buildroot}%{_datadir}/branding/default/backgrounds
cp schema/background.xml %{buildroot}%{_datadir}/branding/default/backgrounds
cp schema/tizen-branding.gschema.override %{buildroot}/usr/share/glib-2.0/schemas/


mkdir -p %{buildroot}%{_datadir}/plymouth/themes
cp syslinux/* %{buildroot}%{_datadir}/branding/default/syslinux
cp -a plymouth/tizen %{buildroot}%{_datadir}/plymouth/themes

%post
%glib2_gsettings_schema_post

%postun
%glib2_gsettings_schema_postun


%files
%manifest %{name}.manifest
%{_datadir}/branding/default/syslinux
%{_datadir}/plymouth/themes/tizen
/usr/share/glib-2.0/schemas/*.override
%{_datadir}/branding/default/backgrounds
