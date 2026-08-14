import { db } from "./firebase.js";
import { collection, addDoc, getDocs } from "firebase/firestore";

async function testFirestore() {
  try {
    // 1. เพิ่มรายการแจ้งซ่อมทดสอบ
    const docRef = await addDoc(collection(db, "repair_orders"), {
      device: "Notebook Dell Vostro",
      problem: "เปิดไม่ติด ชาร์จไฟไม่เข้า",
      status: "pending",
      createdAt: new Date()
    });
    console.log("✅ บันทึกงานซ่อมสำเร็จ ID:", docRef.id);

    // 2. ดึงรายการงานซ่อมทั้งหมดมาแสดง
    const querySnapshot = await getDocs(collection(db, "repair_orders"));
    console.log("📋 รายการงานซ่อมในระบบ:");
    querySnapshot.forEach((doc) => {
      console.log(`- [${doc.id}]`, doc.data());
    });
  } catch (error) {
    console.error("❌ เกิดข้อผิดพลาด:", error.message);
  }
}

testFirestore();