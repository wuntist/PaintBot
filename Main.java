import javax.swing.ImageIcon;
import javax.swing.JFrame;

public class Main {

    public static void main(String[] args) {

        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("PaintBot");
        frame.setSize(1000,500);
        frame.setAlwaysOnTop(false);
        frame.setResizable(false);
        frame.setVisible(true);

        ImageIcon image = new ImageIcon("icon.png");
        frame.setIconImage(image.getImage());
    }
}