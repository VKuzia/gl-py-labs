#version 330

#if defined VERTEX_SHADER

in vec3 in_position;
in vec3 in_normal;
in vec2 in_texcoord_0;

uniform mat4 model;
uniform mat4 view;
uniform mat4 proj;

out vec2 uv;

void main() {
    gl_Position = proj * view * model * vec4(in_position, 1.0);
    uv = in_texcoord_0;
}

#elif defined FRAGMENT_SHADER

uniform sampler2D image;
in vec2 uv;
out vec4 out_color;

void main() {
    out_color = texture(image, uv);
}
#endif