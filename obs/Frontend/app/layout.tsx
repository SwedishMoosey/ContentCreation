import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "../styling/globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <p className="text-7xl font-bold m-4">Streaming Control Panel</p>
        {children}
      </body>
    </html>
  );
}
