// package org.example;

import com.github.kwhat.jnativehook.GlobalScreen;
import com.github.kwhat.jnativehook.NativeHookException;
import com.github.kwhat.jnativehook.keyboard.NativeKeyEvent;
import com.github.kwhat.jnativehook.keyboard.NativeKeyListener;
import com.jcraft.jsch.*;
import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.util.concurrent.atomic.AtomicInteger;

public class Main {
    // ???????
    public static final String host = "62.234.58.121";
    public static final String username = "root";
    public static final String password = "wsh520Lihui@";
    public static final int port = 22; // ??SSH???
    public static AtomicInteger num = new AtomicInteger(0);

    public static void main(String[] args) {
        try {
            // ?? JNativeHook ??
            System.setProperty("java.util.logging.config.file", "/dev/null");

            // ?? JNativeHook
            GlobalScreen.registerNativeHook();
        } catch (NativeHookException ex) {
            System.err.println("Failed to register native hook: " + ex.getMessage());
            return;
        }

        // ???????????
        GlobalScreen.addNativeKeyListener(new NativeKeyListener() {
            @Override
            public void nativeKeyPressed(NativeKeyEvent e) {
                if (e.getKeyCode() == NativeKeyEvent.VC_F8) {
                    takeScreenshot();
                }
            }

            @Override
            public void nativeKeyReleased(NativeKeyEvent e) {
            }

            @Override
            public void nativeKeyTyped(NativeKeyEvent e) {
            }
        });

        System.out.println("Application started successfully. Press F8 to take screenshot.");
    }

    private static void takeScreenshot() {
        try {
            // ?? Robot ??
            Robot robot = new Robot();

            // ??????
            Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
            Rectangle screenRect = new Rectangle(screenSize);

            // ??????
            BufferedImage image = robot.createScreenCapture(screenRect);

            // ????? PNG ??
            File file = new File("screenshot.png");
            ImageIO.write(image, "png", file);

            System.out.println("Screenshot saved to: " + file.getAbsolutePath());

            if (image != null) {
                try {
                    // ??????????
                    ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
                    ImageIO.write(image, "png", outputStream);
                    byte[] imageData = outputStream.toByteArray();

                    // ??????????
                    uploadFile(host, username, password, port, num.getAndIncrement() + ".png", imageData);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void uploadFile(String host, String username, String password, int port, String fileName,
            byte[] data) {
        try {
            // ?? JSch ??
            JSch jsch = new JSch();

            // ?????
            Session session = jsch.getSession(username, host, port);
            session.setPassword(password);
            session.setConfig("StrictHostKeyChecking", "no");
            session.connect();

            // ??SFTP??
            ChannelSftp sftpChannel = (ChannelSftp) session.openChannel("sftp");
            sftpChannel.connect();

            // ????
            ByteArrayInputStream inputStream = new ByteArrayInputStream(data);
            sftpChannel.cd("/usr/local/data");
            sftpChannel.put(inputStream, fileName);

            // ????
            sftpChannel.disconnect();
            session.disconnect();
            System.out.println("File uploaded successfully to /usr/local/data/" + fileName);
        } catch (Exception e) {
            System.out.println("File upload failed!");
            e.printStackTrace();
        }
    }
}
