FasdUAS 1.101.10   ��   ��    k             l      ��  ��   ,&    wifiTunes is a web based remote interface to your favorite music app
    Copyright (C) 2008  Urs Kofmel

    This file is part of wifiTunes.

    wifiTunes is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    wifiTunes is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with wifiTunes.  If not, see <http://www.gnu.org/licenses/>.     � 	 	L          w i f i T u n e s   i s   a   w e b   b a s e d   r e m o t e   i n t e r f a c e   t o   y o u r   f a v o r i t e   m u s i c   a p p  
         C o p y r i g h t   ( C )   2 0 0 8     U r s   K o f m e l  
  
         T h i s   f i l e   i s   p a r t   o f   w i f i T u n e s .  
  
         w i f i T u n e s   i s   f r e e   s o f t w a r e :   y o u   c a n   r e d i s t r i b u t e   i t   a n d / o r   m o d i f y  
         i t   u n d e r   t h e   t e r m s   o f   t h e   G N U   G e n e r a l   P u b l i c   L i c e n s e   a s   p u b l i s h e d   b y  
         t h e   F r e e   S o f t w a r e   F o u n d a t i o n ,   e i t h e r   v e r s i o n   3   o f   t h e   L i c e n s e ,   o r  
         ( a t   y o u r   o p t i o n )   a n y   l a t e r   v e r s i o n .  
  
         w i f i T u n e s   i s   d i s t r i b u t e d   i n   t h e   h o p e   t h a t   i t   w i l l   b e   u s e f u l ,  
         b u t   W I T H O U T   A N Y   W A R R A N T Y ;   w i t h o u t   e v e n   t h e   i m p l i e d   w a r r a n t y   o f  
         M E R C H A N T A B I L I T Y   o r   F I T N E S S   F O R   A   P A R T I C U L A R   P U R P O S E .     S e e   t h e  
         G N U   G e n e r a l   P u b l i c   L i c e n s e   f o r   m o r e   d e t a i l s .  
  
         Y o u   s h o u l d   h a v e   r e c e i v e d   a   c o p y   o f   t h e   G N U   G e n e r a l   P u b l i c   L i c e n s e  
         a l o n g   w i t h   w i f i T u n e s .     I f   n o t ,   s e e   < h t t p : / / w w w . g n u . o r g / l i c e n s e s / > .    
  
 l     ��������  ��  ��        i         I     �� ��
�� .aevtoappnull  �   � ****  o      ���� 0 	arguments  ��    Z     �  ����  =        n         m    ��
�� 
nmbr  n         2   ��
�� 
cobj  o     ���� 0 	arguments    m    ����   k   
 �       r   
     n   
     4    ��  
�� 
cobj   m    ����   o   
 ���� 0 	arguments    o      ���� 0 
workingdir 
WorkingDir   ! " ! r     # $ # n     % & % 4    �� '
�� 
cobj ' m    ����  & o    ���� 0 	arguments   $ o      ���� 0 playlistlist PlaylistList "  (�� ( O    � ) * ) k    � + +  , - , r    ! . / . 2   ��
�� 
cUsP / o      ���� 0 allplaylists AllPlaylists -  0 1 0 r   " - 2 3 2 l  " + 4���� 4 I  " +�� 5 6
�� .rdwropenshor       file 5 l  " % 7���� 7 b   " % 8 9 8 o   " #���� 0 
workingdir 
WorkingDir 9 o   # $���� 0 playlistlist PlaylistList��  ��   6 �� :��
�� 
perm : m   & '��
�� boovtrue��  ��  ��   3 o      ���� 0 playlistsfile PlaylistsFile 1  ; < ; I  . 5�� = >
�� .rdwrseofnull���     **** = o   . /���� 0 playlistsfile PlaylistsFile > �� ?��
�� 
set2 ? m   0 1����  ��   <  @�� @ Q   6 � A B C A k   9 � D D  E F E l  9 9�� G H��   G N Hwrite "items :" & (count of items of playlists) to PlaylistsFile as text    H � I I � w r i t e   " i t e m s   : "   &   ( c o u n t   o f   i t e m s   o f   p l a y l i s t s )   t o   P l a y l i s t s F i l e   a s   t e x t F  J K J l  9 9�� L M��   L 1 +write (ASCII character 10) to PlaylistsFile    M � N N V w r i t e   ( A S C I I   c h a r a c t e r   1 0 )   t o   P l a y l i s t s F i l e K  O P O X   9 � Q�� R Q k   I � S S  T U T r   I N V W V l  I L X���� X n   I L Y Z Y 1   J L��
�� 
pnam Z o   I J���� 0 thisplaylist ThisPlaylist��  ��   W o      ���� 0 thename TheName U  [ \ [ r   O \ ] ^ ] c   O X _ ` _ l  O T a���� a n   O T b c b 1   P T��
�� 
pidx c o   O P���� 0 thisplaylist ThisPlaylist��  ��   ` m   T W��
�� 
ctxt ^ o      ���� 0 theindex TheIndex \  d e d Z   ] � f g�� h f =  ] d i j i n   ] b k l k 1   ^ b��
�� 
pSmt l o   ] ^���� 0 thisplaylist ThisPlaylist j m   b c��
�� boovtrue g I  g z�� m n
�� .rdwrwritnull���     **** m m   g j o o � p p  s m a r t : n �� q r
�� 
refn q o   m n���� 0 playlistsfile PlaylistsFile r �� s��
�� 
as   s m   q t��
�� 
ctxt��  ��   h I  } ��� t u
�� .rdwrwritnull���     **** t m   } � v v � w w  n o r m a l : u �� x y
�� 
refn x o   � ����� 0 playlistsfile PlaylistsFile y �� z��
�� 
as   z m   � ���
�� 
ctxt��   e  { | { I  � ��� } ~
�� .rdwrwritnull���     **** } l  � � ����  b   � � � � � o   � ����� 0 theindex TheIndex � m   � � � � � � �  :��  ��   ~ �� � �
�� 
refn � o   � ����� 0 playlistsfile PlaylistsFile � �� ���
�� 
as   � m   � ���
�� 
ctxt��   |  � � � I  � ��� � �
�� .rdwrwritnull���     **** � o   � ����� 0 thename TheName � �� � �
�� 
refn � o   � ����� 0 playlistsfile PlaylistsFile � �� ���
�� 
as   � m   � ���
�� 
utf8��   �  ��� � I  � ��� � �
�� .rdwrwritnull���     **** � l  � � ����� � I  � ��� ���
�� .sysontocTEXT       shor � m   � ����� 
��  ��  ��   � �� ���
�� 
refn � o   � ����� 0 playlistsfile PlaylistsFile��  ��  �� 0 thisplaylist ThisPlaylist R o   < =���� 0 allplaylists AllPlaylists P  ��� � I  � ��� ���
�� .rdwrclosnull���     **** � o   � ����� 0 playlistsfile PlaylistsFile��  ��   B R      ������
�� .ascrerr ****      � ****��  ��   C I  � ��� ���
�� .rdwrclosnull���     **** � o   � ����� 0 playlistsfile PlaylistsFile��  ��   * m     � ��                                                                                  hook   alis    :  System                     �QOH+     �
iTunes.app                                                      W�ñ��        ����  	                Applications    �P�/      ñ��       �  System:Applications:iTunes.app   
 i T u n e s . a p p    S y s t e m  Applications/iTunes.app   / ��  ��  ��  ��     ��� � l     ��������  ��  ��  ��       �� � ���   � ��
�� .aevtoappnull  �   � **** � �� ���� � ���
�� .aevtoappnull  �   � ****�� 0 	arguments  ��   � ������ 0 	arguments  �� 0 thisplaylist ThisPlaylist � !�������� ���������~�}�|�{�z�y�x�w�v�u�t o�s�r�q�p v ��o�n�m�l�k�j
�� 
cobj
�� 
nmbr�� 0 
workingdir 
WorkingDir�� 0 playlistlist PlaylistList
�� 
cUsP�� 0 allplaylists AllPlaylists
�� 
perm
� .rdwropenshor       file�~ 0 playlistsfile PlaylistsFile
�} 
set2
�| .rdwrseofnull���     ****
�{ 
kocl
�z .corecnte****       ****
�y 
pnam�x 0 thename TheName
�w 
pidx
�v 
ctxt�u 0 theindex TheIndex
�t 
pSmt
�s 
refn
�r 
as  �q 
�p .rdwrwritnull���     ****
�o 
utf8�n 

�m .sysontocTEXT       shor
�l .rdwrclosnull���     ****�k  �j  �� ��-�,l  ޠ�k/E�O��l/E�O� �*�-E�O��%�el E�O��jl O � ��[��l kh ��,E�O�a ,a &E` O�a ,e  a a �a a a  Y a a �a a a  O_ a %a �a a a  O�a �a a a  Oa j a �l [OY�yO�j W X   �j UY h ascr  ��ޭ