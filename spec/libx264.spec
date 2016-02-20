Summary:     libx264
Name:        libx264
Version:     148
Release:     1
License:     GPLv2
Group:       Applications/Multimedia
URL:         http://www.videolan.org/developers/x264.html
Source:      libx264-148.tar.gz

%description
The libx264 codec implementation

%prep
%setup -q -n x264

%build
%configure --enable-shared --prefix=/usr
make %{?jobs:-j%jobs}

%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/bin/x264
/usr/include/x264.h
/usr/include/x264_config.h
/usr/lib/pkgconfig/x264.pc
/usr/lib/libx264.so
/usr/lib/libx264.so.148

