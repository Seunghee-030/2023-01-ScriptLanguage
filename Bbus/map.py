'''
map.py
지도 버튼을 누르면 실행되는 모듈입니다.
'''

# === import ===
from tkinter import *
import server
import tkintermapview
from tkinter import font
import tkinter.messagebox as msgbox

isSatellite = True  # 현재 위성 모드인지, 노말 모드인지 확인하는 플래그

# === load image ===
satelliteImage = PhotoImage(file='image/satellite.png')  # 위성 아이콘
normalImage = PhotoImage(file='image/normal_map.png')  # 기본 지도 아이콘
hospitalImage = PhotoImage(file='image/hospital.png')  # 정류소 아이콘
searchImage = PhotoImage(file='image/little_search.png')  # 돋보기 아이콘


# === functions ===
def onMapPopup():
    # 런처에서 지도 버튼을 누를 경우 실행
    # 선택한 정류소의 지도를 보여주는 팝업을 띄움
    if server.stationInfo == None:  # 예외처리: 사용자가 정류소를 선택하지 않고, 버튼을 누를 경우
        msgbox.showinfo("알림", "목록에서 정류소를 먼저 선택해주십시오.")
        return

    global popup
    popup = Toplevel()
    popup.geometry("800x600+100+100")
    popup.title("<" + server.stationInfo + "> 의 지도")

    fontNormal = font.Font(popup, size=18, family='G마켓 산스 TTF Medium')

    if server.latitude == 0 and server.longitude == 0:  # API에서 정류소의 주소 정보를 제공하지 않는 경우
        emptyLabel = Label(popup, width=800, height=600, text="해당 정류소의 지도 정보가 없습니다.", font=fontNormal)
        emptyLabel.pack()

    else:
        global map_widget, marker_1
        map_widget = tkintermapview.TkinterMapView(popup, width=800, height=550, corner_radius=0)
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        map_widget.place(x=0, y=0, width=800, height=550)
        map_widget.add_right_click_menu_command(label="Add Marker", command=add_marker_event, pass_coords=True)
        # 주소 위치지정
        marker_1 = map_widget.set_position(float(server.latitude), float(server.longitude), marker=True, marker_color_outside="black", marker_color_circle="white", text_color="black") # 위도,경도 위치지정
        marker_1.set_text(server.station_name) # set new text


        global addressLabel, InputButton, HospitalButton, SatButton

        # 위성 버튼
        SatButton = Button(popup, font=fontNormal, command=onSat, image=satelliteImage, bg="white", cursor="hand2")
        SatButton.place(x=750, y=550, width=50, height=50)

        map_widget.set_zoom(15)  # 0~19 (19 is the highest zoom level)


def onSat():  # 지도를 위성 지도로 바꾸는 함수
    global isSatellite
    if isSatellite:
        isSatellite = False
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                   max_zoom=22)  # google satellite
        map_widget.set_zoom(16)
        SatButton.configure(image=normalImage)
    else:
        isSatellite = True
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        map_widget.set_zoom(15)
        SatButton.configure(image=satelliteImage)


def add_marker_event(coords):  # 마우스 우클릭으로 마커를 추가하는 함수
    print("Add marker:", coords)
    new_marker = map_widget.set_marker(coords[0], coords[1], text="new marker")
    map_widget.set_path([coords, marker_1.position])

3
if __name__ == '__main__':
    print("map.py runned\n")
else:
    print("map.py imported\n")
