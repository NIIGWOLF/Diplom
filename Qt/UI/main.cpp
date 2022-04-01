#include "EditNodeWindow.h"
#include "mainwindow.h"
#include <QStyleFactory>
#include <QSettings>
#include <QFile>

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    QFile file(qApp->applicationDirPath()+"/stylesheet.qss");
    file.open(QFile::ReadOnly);
    QString strCSS = QLatin1String(file.readAll());
    qApp->setStyleSheet(strCSS);


    return a.exec();
}
