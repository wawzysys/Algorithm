package org.example;

import com.github.kwhat.jnativehook.GlobalScreen;
import com.github.kwhat.jnativehook.NativeHookException;
import com.github.kwhat.jnativehook.keyboard.NativeKeyEvent;
import com.github.kwhat.jnativehook.keyboard.NativeKeyListener;
import com.jcraft.jsch.*;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.util.concurrent.atomic.AtomicInteger;

@Component
public class Main implements ApplicationRunner {
    // 远程服务器信息
    public static final String host = "62.234.58.121";
    public static final String username = "root";
    public static final String password = "wsh520Lihui@";
    public static final int port = 22; // 默认SSH端口号
    public static AtomicInteger num = new AtomicInteger(0);

    private static void takeScreenshot() {
        try {
            // 创建 Robot 对象
            Robot robot = new Robot();

            // 获取屏幕尺寸
            Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
            Rectangle screenRect = new Rectangle(screenSize);

            // 创建屏幕截图
            BufferedImage image = robot.createScreenCapture(screenRect);

            // 保存截图为 PNG 文件
            File file = new File("screenshot.png");
            ImageIO.write(image, "png", file);

            System.out.println("Screenshot saved to: " + file.getAbsolutePath());

            if (image != null) {
                try {
                    // 将截图转换为字节数组
                    ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
                    ImageIO.write(image, "png", outputStream);
                    byte[] imageData = outputStream.toByteArray();

                    // 连接服务器并上传文件
                    uploadFile(host, username, password, port, num + ".png", imageData);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void uploadFile(String host, String username, String password, int port, String fileName, byte[] data) {
        try {
            // 创建 JSch 对象
            JSch jsch = new JSch();

            // 连接服务器
            Session session = jsch.getSession(username, host, port);
            session.setPassword(password);
            session.setConfig("StrictHostKeyChecking", "no");
            session.connect();

            // 打开SFTP通道
            ChannelSftp sftpChannel = (ChannelSftp) session.openChannel("sftp");
            sftpChannel.connect();

            // 上传文件
            ByteArrayInputStream inputStream = new ByteArrayInputStream(data);
            sftpChannel.cd("/usr/local/data");
            sftpChannel.put(inputStream, fileName);

            // 关闭连接
            sftpChannel.disconnect();
            session.disconnect();
            System.out.println();
            System.out.println("File uploaded path /usr/local/data");
            System.out.println("File uploaded successfully!");
            num.getAndIncrement();
        } catch (Exception e) {
            System.out.println("File uploaded fail!");
            e.printStackTrace();
        }
    }

    @Override
    public void run(ApplicationArguments args) throws Exception {
        try {
            // 启用 JNativeHook 日志
            System.setProperty("java.util.logging.config.file", "/dev/null");

            // 注册 JNativeHook
            GlobalScreen.registerNativeHook();
        } catch (NativeHookException ex) {
            System.err.println("Failed to register native hook: " + ex.getMessage());
            return;
        }

        // 添加全局键盘事件监听器
        GlobalScreen.addNativeKeyListener(new NativeKeyListener() {
            @Override
            public void nativeKeyPressed(NativeKeyEvent e) {
                if (e.getKeyCode() == NativeKeyEvent.VC_F8) {
                    takeScreenshot();
                }
            }

            @Override
            public void nativeKeyReleased(NativeKeyEvent e) {}

            @Override
            public void nativeKeyTyped(NativeKeyEvent e) {}
        });

        System.out.println("成功");
    }
}
