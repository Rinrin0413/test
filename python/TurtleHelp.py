#[{(Imports)}]
from turtle import *#Turtleモジュール
import random#乱数生成モジュール

#{(見た目)}
shape("classic")#芯の見た目を決める{arrow(↑),turtle(🐢),circle(●),square(■),triangle(▲),classic(➤)}
#{(移動,描画)}
forward(50)#向いている方向に直進して描画(負の数も利用可能)
fd(0)#↑〃
backward(100)#後ろに直進して描画(負の数も利用可能)
back(0)#↑〃
bk(0)#↑〃
right(45)#右にアングルを変更(度数で記載)
rt(0)#↑〃
left(90)#左にアングルを変更(度数で記載)
lt(0)#↑〃
setposition(100, 100)#指定した座標に移動しながら描画(xy座標)
setpos(-100, -100)#↑〃
goto(100, 100)#↑〃
setx(10)#X座標を指定して移動させながら描画
setheading(0)#回転させる(北が90)
seth(180)#↑〃
home()#原点に戻り指定も初期化しながら描画
circle(40, extent=280, steps=8)#円を描画(半径が数値でextentが書く弧の角度,stepsは辺の数)
dot(20, "red")#塗りつぶされた●を描く(直径とカラーを記入)
stamp()#亀形のスタンプをする
undo()#一回分元に戻す(forで回数指定可能)
speed(speed=10)#描画速度を設定する(最遅1,遅3,普通6,速10,最速0)

#[{(情報取得)}]
print(position())#現在座標を取得
print(pos())#↑〃
print(towards(0, 0))#現在位置からの指定した座標への角度を取得
print(xcor())#現在のx座標を取得
print(ycor())#現在のy座標を取得
print(heading())#現在のアングルを取得
print(distance(0, 0))#現在位置からの指定した座標までの距離を取得

#[{(描画状態)}]
pendown()#ペンを降ろす
down()#↑〃
pd()#↑〃
penup()#ペンを上げる
up()#↑〃
pu()#↑〃
pensize(width=100)#ペンのサイズを変更
width(width=10)#↑〃
print(isdown())#ペンが下がってるかを検知

#[{(色の制御)}]
color("#7700FF")#色を変更

#[{(敷き詰め)}]
begin_fill()#fillの始点をセット
goto(200, -300)
goto(200, -0)
end_fill()#fillの終点をセットして埋める

#[{(更なる制御)}]
reset()#変数含め全てをリセット
clear()#描いた物のみ削除します
color("#FFD000")
write("🤔", move=False, align="left")#文字を書く(moveは右下に表示するか,alignは"left","center","right")

done()#とりま書いとけ


