#! /bin/sh 

DIR=`pwd`
FILE=$DIR/$1
TEMP=$DIR/$1.temp
sed '/^[[:space:]]*$/d' $FILE > $TEMP
cp $TEMP $FILE
rm $TEMP
