#pragma OPENCL EXTENSION cl_khr_fp64 : enable
__kernel void vnorm(
	 global double  * vecs,
	 global double  * mods )
{
	size_t i = get_global_id(0);
	double3 v = vload3(i, vecs);
        mods[i] = sqrt( v.x *v.x + v.y *v.y + v.z *v.z );
}