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
 l     ��������  ��  ��     ��  i         I     �� ��
�� .aevtoappnull  �   � ****  o      ���� 0 	arguments  ��    Z    �  ����  =        n         m    ��
�� 
nmbr  n         2   ��
�� 
cobj  o     ���� 0 	arguments    m    ����   k   
�       l  
 
��  ��     	say "one"     �    s a y   " o n e "      r   
    !   n   
  " # " 4    �� $
�� 
cobj $ m    ����  # o   
 ���� 0 	arguments   ! o      ���� 0 
workingdir 
WorkingDir   % & % l   �� ' (��   ' > 8set WorkingDir to "/Users/coffee/bin/pyituneswebremote/"    ( � ) ) p s e t   W o r k i n g D i r   t o   " / U s e r s / c o f f e e / b i n / p y i t u n e s w e b r e m o t e / " &  * + * r     , - , n     . / . 4    �� 0
�� 
cobj 0 m    ����  / o    ���� 0 	arguments   - o      ���� 0 outputsname OutputsName +  1 2 1 l   �� 3 4��   3 &  set OutputsName to "outputs.txt"    4 � 5 5 @ s e t   O u t p u t s N a m e   t o   " o u t p u t s . t x t " 2  6 7 6 l   �� 8 9��   8  	say "two"    9 � : :  s a y   " t w o " 7  ; < ; I   �� =��
�� .sysoexecTEXT���     TEXT = m     > > � ? ? . k i l l a l l   ' S y s t e m   E v e n t s '��   <  @�� @ O   � A B A k   "� C C  D E D r   " ( F G F 4   " &�� H
�� 
prcs H m   $ % I I � J J  i T u n e s G o      ���� 0 
itunesproc 
iTunesProc E  K L K r   ) / M N M n   ) - O P O 4   * -�� Q
�� 
uiel Q m   + , R R � S S  i T u n e s P o   ) *���� 0 
itunesproc 
iTunesProc N o      ���� 0 
mainwindow 
MainWindow L  T U T r   0 5 V W V m   0 1��
�� boovtrue W n       X Y X 1   2 4��
�� 
pisf Y o   1 2���� 0 
itunesproc 
iTunesProc U  Z�� Z Q   6� [ \ ] [ k   90 ^ ^  _ ` _ l  9 D a b c a e   9 D d d n   9 D e f e 4  @ C�� g
�� 
menI g m   A B������ f n   9 @ h i h 4   = @�� j
�� 
uiel j m   > ?����  i 4   9 =�� k
�� 
prcs k m   ; < l l � m m  i T u n e s b # only possible if already open    c � n n : o n l y   p o s s i b l e   i f   a l r e a d y   o p e n `  o p o r   E T q r q n   E P s t s 2   N P��
�� 
menI t n   E N u v u 4   K N�� w
�� 
uiel w m   L M����  v 4   E K�� x
�� 
prcs x m   G J y y � z z  i T u n e s r o      ���� 0 thelist TheList p  { | { r   U Z } ~ } m   U V��
�� boovtrue ~ o      ���� 0 
keepadding 
KeepAdding |   �  r   [ a � � � J   [ ]����   � o      ���� 0 outputs Outputs �  � � � X   b � ��� � � Q   v � � � � � k   y � � �  � � � r   y � � � � n   y ~ � � � 1   z ~��
�� 
pnam � o   y z���� 0 thisitem ThisItem � o      ���� 0 itemname ItemName �  ��� � Z   � � � ����� � o   � ����� 0 
keepadding 
KeepAdding � r   � � � � � b   � � � � � o   � ����� 0 outputs Outputs � J   � � � �  ��� � o   � ����� 0 itemname ItemName��   � o      ���� 0 outputs Outputs��  ��  ��   � R      ������
�� .ascrerr ****      � ****��  ��   � r   � � � � � m   � ���
�� boovfals � o      ���� 0 
keepadding 
KeepAdding�� 0 thisitem ThisItem � o   e h���� 0 thelist TheList �  � � � I  � ��� ���
�� .prcskcodnull���    long � m   � ����� 5��   �  ��� � O   �0 � � � k   �/ � �  � � � r   � � � � � l  � � ����� � I  � ��� � �
�� .rdwropenshor       file � l  � � ����� � b   � � � � � o   � ����� 0 
workingdir 
WorkingDir � o   � ����� 0 outputsname OutputsName��  ��   � �� ���
�� 
perm � m   � ���
�� boovtrue��  ��  ��   � o      ���� 0 outputsfile OutputsFile �  � � � I  � ��� � �
�� .rdwrseofnull���     **** � o   � ����� 0 outputsfile OutputsFile � �� ���
�� 
set2 � m   � �����  ��   �  ��� � Q   �/ � � � � k   �  � �  � � � X   � ��� � � k   � � �  � � � I  ��� � �
�� .rdwrwritnull���     **** � o   � ����� 0 
thisoutput 
ThisOutput � �� � �
�� 
refn � o   � ����� 0 outputsfile OutputsFile � �� ���
�� 
as   � m   � ���
�� 
utf8��   �  ��� � I �� � �
�� .rdwrwritnull���     **** � l 	 ����� � I 	�� ���
�� .sysontocTEXT       shor � m  ���� 
��  ��  ��   � �� ���
�� 
refn � o  ���� 0 outputsfile OutputsFile��  ��  �� 0 
thisoutput 
ThisOutput � o   � ����� 0 outputs Outputs �  ��� � I  �� ���
�� .rdwrclosnull���     **** � o  ���� 0 outputsfile OutputsFile��  ��   � R      ������
�� .ascrerr ****      � ****��  ��   � I (/�� ���
�� .rdwrclosnull���     **** � o  (+���� 0 outputsfile OutputsFile��  ��   � m   � � � ��                                                                                  hook   alis    :  System                     �QOH+     �
iTunes.app                                                      W�ñ��        ����  	                Applications    �P�/      ñ��       �  System:Applications:iTunes.app   
 i T u n e s . a p p    S y s t e m  Applications/iTunes.app   / ��  ��   \ R      ������
�� .ascrerr ****      � ****��  ��   ] O  8� � � � k  >� � �  � � � r  >M � � � l >I ����� � I >I�� � �
�� .rdwropenshor       file � l >A ���� � b  >A � � � o  >?�~�~ 0 
workingdir 
WorkingDir � o  ?@�}�} 0 outputsname OutputsName��  �   � �| ��{
�| 
perm � m  DE�z
�z boovtrue�{  ��  ��   � o      �y�y 0 outputsfile OutputsFile �  � � � I NY�x � �
�x .rdwrseofnull���     **** � o  NQ�w�w 0 outputsfile OutputsFile � �v ��u
�v 
set2 � m  TU�t�t  �u   �  ��s � Q  Z� � � � � k  ]z � �  � � � I ]r�r � �
�r .rdwrwritnull���     **** � m  ]` � � � � �  n o t   e n a b l e d � �q � �
�q 
refn � o  cf�p�p 0 outputsfile OutputsFile � �o ��n
�o 
as   � m  il�m
�m 
ctxt�n   �  ��l � I sz�k ��j
�k .rdwrclosnull���     **** � o  sv�i�i 0 outputsfile OutputsFile�j  �l   � R      �h�g�f
�h .ascrerr ****      � ****�g  �f   � I ���e ��d
�e .rdwrclosnull���     **** � o  ���c�c 0 outputsfile OutputsFile�d  �s   � m  8; � ��                                                                                  hook   alis    :  System                     �QOH+     �
iTunes.app                                                      W�ñ��        ����  	                Applications    �P�/      ñ��       �  System:Applications:iTunes.app   
 i T u n e s . a p p    S y s t e m  Applications/iTunes.app   / ��  ��   B m     � ��                                                                                  sevs   alis    |  System                     �QOH+     �System Events.app                                                �	�oP>        ����  	                CoreServices    �P�/      �oB.       �   Q   P  4System:System:Library:CoreServices:System Events.app  $  S y s t e m   E v e n t s . a p p    S y s t e m  -System/Library/CoreServices/System Events.app   / ��  ��  ��  ��  ��       �b � ��b   � �a
�a .aevtoappnull  �   � **** � �` �_�^ � ��]
�` .aevtoappnull  �   � ****�_ 0 	arguments  �^   � �\�[�Z�\ 0 	arguments  �[ 0 thisitem ThisItem�Z 0 
thisoutput 
ThisOutput � ,�Y�X�W�V >�U ��T I�S�R R�Q�P l�O y�N�M�L�K�J�I�H�G�F�E�D ��C�B�A�@�?�>�=�<�;�:�9�8�7 ��6
�Y 
cobj
�X 
nmbr�W 0 
workingdir 
WorkingDir�V 0 outputsname OutputsName
�U .sysoexecTEXT���     TEXT
�T 
prcs�S 0 
itunesproc 
iTunesProc
�R 
uiel�Q 0 
mainwindow 
MainWindow
�P 
pisf
�O 
menI�N 0 thelist TheList�M 0 
keepadding 
KeepAdding�L 0 outputs Outputs
�K 
kocl
�J .corecnte****       ****
�I 
pnam�H 0 itemname ItemName�G  �F  �E 5
�D .prcskcodnull���    long
�C 
perm
�B .rdwropenshor       file�A 0 outputsfile OutputsFile
�@ 
set2
�? .rdwrseofnull���     ****
�> 
refn
�= 
as  
�< 
utf8�; 
�: .rdwrwritnull���     ****�9 

�8 .sysontocTEXT       shor
�7 .rdwrclosnull���     ****
�6 
ctxt�]���-�,l ���k/E�O��l/E�O�j O�j*��/E�O���/E�Oe��,FO �*��/�l/�i/EO*�a /�l/�-E` OeE` OjvE` O I_ [a �l kh  &�a ,E` O_  _ _ kv%E` Y hW X  fE` [OY��Oa j Oa  v��%a el E` O_ a  jl !O K =_ [a �l kh �a "_ a #a $a % &Oa 'j (a "_ l &[OY��O_ j )W X  _ j )UW YX  a  M��%a el E` O_ a  jl !O "a *a "_ a #a +a % &O_ j )W X  _ j )UUY h ascr  ��ޭ