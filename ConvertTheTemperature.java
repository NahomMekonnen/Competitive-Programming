import java.text.DecimalFormat;

public class ConvertTheTemperature {

    public double[] convertTemperature(double celsius) {
        DecimalFormat df=new DecimalFormat("0.00000");
        double fahrenheit, kelvin;
        fahrenheit= Double.parseDouble(df.format(celsius*1.80+32));
        kelvin=Double.parseDouble(df.format(celsius+273.15));
        double[] ans={kelvin,fahrenheit};
        return ans;

    }
}
