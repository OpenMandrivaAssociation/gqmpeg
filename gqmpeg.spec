%define version 0.91.1
%define release %mkrel 3
%define name 	gqmpeg

Summary: 	Graphical Frontend to various music players
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License:	GPL
Group: 		Sound
URL: 		http://gqmpeg.sourceforge.net/
BuildRoot: 	%_tmppath/%{name}-%{version}-%{release}-buildroot
Source: 	ftp://osdn.dl.sourceforge.net/pub/sourceforge/g/gq/%{name}/%{name}-%{version}.tar.bz2
Patch0:		gqmpeg-0.91.1-no-translation.patch
Buildrequires:	gtk2-devel >= 2.2.0
BuildRequires:	png-devel

Requires:	mpg123 >= 0.59
Requires:	vorbis-tools
# (Abel) not adding xmp for now
#Requires:	xmp

%description
GQmpeg is a graphical frontend to various command line
music players. It includes playlist support and all the
usual playing features. random, repeat, etc.; and it supports
custom skins (looks).

%prep
%setup -q
%patch0 -p1 -b .no-translation

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%{find_lang} %{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application <<EOF
Exec=%{_bindir}/gqmpeg 
Name=Gqmpeg 
Comment=Graphical Frontend of Audio Players 
Icon=sound_section 
Categories=Audio;
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)

%doc README COPYING FAQ TODO SKIN-SPECS SKIN-SPECS-V1 plugin/README.plugin
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop

